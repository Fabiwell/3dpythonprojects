import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

quandl.api_config.ApiConfig.api_key = 'rgqtzopHyVJ4KbbSmCHV'
style.use('ggplot')

data = quandl.get('BCHAIN/MKPRU')
data = data[['Value']]
# data['HL_PCT'] = (data['Adj. High'] - data['Adj. Close']) / data['Adj. Close'] * 100
# data['PCT_change'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100

# data = data[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Value'
data.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.001*len(data)))

data['label'] = data[forecast_col].shift(-forecast_out)



X = np.array(data.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

data.dropna(inplace=True)
y = np.array(data['label'])

X_train, X_test, y_train, y_test =  model_selection.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf, f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)
# print(forecast_set, accuracy, forecast_out)
data['Forecast'] = np.nan

last_date = data.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    data.loc[next_date] = [np.nan for _ in range(len(data.columns) -1)] + [i]

print(data.tail())

data['Value'].plot()
data['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()