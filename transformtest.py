# translate.py
import numpy as np

# Define a set of Cartesian (x, y, z) points
point_cloud = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [1, 2, 3],
]

# Convert to homogeneous coordinates
point_cloud_homogeneous = []
for point in point_cloud:
    point_homogeneous = point.copy()
    point_homogeneous.append(1)
    point_cloud_homogeneous.append(point_homogeneous)

# Define the translation
tx = 2
ty = 10
tz = 100

# Construct the translation matrix
translation_matrix = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [tx, ty, tz, 1],
]

# Apply the transformation to our point cloud
translated_points = np.matmul(
    point_cloud_homogeneous,
    translation_matrix)

# Convert to cartesian coordinates
translated_points_xyz = []
for point in translated_points:
    point = np.array(point[:-1])
    translated_points_xyz.append(point)

# Map original to translated point coordinates
# (x0, y0, z0) → (x1, y1, z1)
for i in range(len(point_cloud)):
    point = point_cloud[i]
    translated_point = translated_points_xyz[i]
    print(f'{point} → {list(translated_point)}')