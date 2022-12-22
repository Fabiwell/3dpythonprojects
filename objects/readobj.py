# from torch_geometric import *


def yield_file(in_file):
    vertices = []
    faces = []
    f = open(in_file)
    buf = f.read()
    f.close()
    for b in buf.split('\n'):
        if b.startswith('v '):
            # b.pop(0)
            b.replace("v", "")
            e = b.split(" ")[2:]
            # for x in e:
                # e[0] = float(x)
            e[0] = float(e[0])
            e[1] = float(e[1])
            e[2] = float(e[2])
            vertices.append(e)
            # print(e)
        # elif b.startswith('f '):
        #     triangle = b.split(' ')[1:]
        #     # -1 as .obj is base 1 but the Data class expects base 0 indices
        #     yield ['f', [[int(i) - 1 for i in t.split("/")] for t in triangle]]
        # else:
        #     yield ['', ""]
    return vertices
    # print(vertices)

# def read_obj(in_file):
#     vertices = []
#     faces = []

#     for k, v in yield_file(in_file):
#         if k == 'v':
#             vertices.append(v)
#         elif k == 'f':
#             for i in v:
#                 faces.append(i)

#     print(vertices)

#     if not len(faces) or not len(vertices):
#         return None

    # pos = torch.tensor(vertices, dtype=torch.float)
    # face = torch.tensor(faces, dtype=torch.long).t().contiguous()

    # data = Data(pos=pos, face=face)

    # return data 

# e = yield_file(r"C:\Users\gebruiker\OneDrive\PythonScript\3dpython\objects\FinalBaseMesh.obj")
# print(e)
# read_obj(r"C:\Users\gebruiker\OneDrive\PythonScript\3dpython\objects\FinalBaseMesh.obj")
# print('s')