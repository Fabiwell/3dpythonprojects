from random import randint
from sre_parse import WHITESPACE
import pygame
import numpy as np
import pywavefront
from math import *
import time

WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Python :)")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)


# def yield_file(in_file):
#     vertices = []
#     faces = []
#     f = open(in_file)
#     buf = f.read()
#     f.close()
#     for b in buf.split('\n'):
#         if b.startswith('v '):
#             # b.pop(0)
#             b.replace("v", "")
#             e = b.split(" ")[1:]
#             # for x in e:
#                 # e[0] = float(x)
#             # print(e)
#             e[0] = float(e[0])
#             e[1] = float(e[1])
#             e[2] = float(e[2])
#             vertices.append(e)
#             # print(e)
#         elif b.startswith('f '):
            
#             # -1 as .obj is base 1 but the Data class expects base 0 indices
#             triangle = b.split(' ')[1:]
#             for t in triangle:
#                 # for i in t.split("/"):
#                     # if i == '':
#                     #     pass
#                     # else:
#                     #     i = int(i)
#                     #     # print(i)
#                 e = t.split("/")
#                 e[0] = int(e[0])
#                 if e[1] is not '':
#                     e[1] = int(e[1])
#                 e[2] = int(e[2])
#                 faces.append(e)
#                 # print(t.split("/"))

#                 # print(e)
#         # else:
#         #     yield ['', ""]
#     return vertices, faces



class object():
    def __init__(self, pos, length, width, height, color, scale):
        self.scale = scale
        self.pos = pos
        self.anglex = 0
        self.angley = 0
        self.anglez = 0
        self.color = color

        self.points = []

        # self.points.append(np.matrix([[-1], [-1], [1]]))
        # self.points.append(np.matrix([[1], [-1], [1]]))
        # self.points.append(np.matrix([[1], [1], [1]]))
        # self.points.append(np.matrix([[-1], [1], [1]]))
        # self.points.append(np.matrix([[-1], [-1], [-1]]))
        # self.points.append(np.matrix([[1], [-1], [-1]]))
        # self.points.append(np.matrix([[1], [1], [-1]]))
        # self.points.append(np.matrix([[-1], [1], [-1]]))
        # vertecies, faces = yield_file(r"C:\Users\gebruiker\OneDrive\PythonScript\3dpython\objects\testobj.obj")
        self.data = pywavefront.Wavefront(r"C:\Users\gebruiker\OneDrive\PythonScript\3dpython\objects\testobj.obj", create_materials=True)
        # print(faces)
        # print(len(vertecies))
        for x in self.data.vertices:
            self.points.append(np.matrix([[x[0]], [x[1]], [x[2]]]))

        # self.faces = self.data.

        self.projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        self.projected_points = [
            [n, n] for n in range(len(self.points))
        ]

    def connect_points(self, i, j, points):
        pygame.draw.line(screen, self.color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

    def draw(self):
        self.rotation_x = np.matrix([
            [1, 0, 0],
            [0, cos(self.anglex), -sin(self.anglex)],
            [0, sin(self.anglex), cos(self.anglex)]
        ])
        self.rotation_y = np.matrix([
            [cos(self.angley), 0, sin(self.angley)],
            [0, 1, 0],
            [-sin(self.angley), 0, cos(self.angley)]
        ])
        self.rotation_z = np.matrix([
            [cos(self.anglez), -sin(self.anglez), 0],
            [sin(self.anglez), cos(self.anglez), 0],
            [0, 0, 1]
        ])
        
        i = 0
        for point in self.points:
            rotated2d = np.dot(self.rotation_z, point)
            rotated2d = np.dot(self.rotation_y, rotated2d)
            rotated2d = np.dot(self.rotation_x, rotated2d)

            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.scale) + self.pos[0]
            y = int(projected2d[1][0] * self.scale) + self.pos[1]

            self.projected_points[i] = [x, y]
            # pygame.draw.circle(screen, BLACK, (x, y), 5)
            i += 1

        # self.connect_points(0, 1, self.projected_points)
        # self.connect_points(1, 2 , self.projected_points)
        # self.connect_points(2, 3, self.projected_points)
        # self.connect_points(3, 0, self.projected_points)

        # self.connect_points(4, 5, self.projected_points)
        # self.connect_points(5, 6, self.projected_points)
        # self.connect_points(6, 7, self.projected_points)
        # self.connect_points(7, 4, self.projected_points)

        # self.connect_points(0, 4, self.projected_points)
        # self.connect_points(1, 5, self.projected_points)
        # self.connect_points(2, 6, self.projected_points)
        # self.connect_points(3, 7, self.projected_points)
        # print(len(self.projected_points))
        for point in self.projected_points:
            for point2 in self.projected_points:
                # print(point[0])
                pygame.draw.line(screen, self.color, (point[0], point[1]), (point2[0], point2[1]))
        # for face in self.faces:
        #     if face[0] <= len(self.projected_points) -1 and face[2] <= len(self.projected_points) -1:
        #         self.connect_points(face[0], face[2], self.projected_points)
            # print(face)





clock = pygame.time.Clock()
obj = object([400, 300], 2, 1, 1, BLACK, 100)
obj.scale = 100
forward = False
backward = False
left = False
right = False
f = False


# obj.angley += 0.5

while True:
    clock.tick(60)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_w:
                forward = True
            if event.key == pygame.K_s:
                backward = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
            
            if event.key == pygame.K_f:
                f = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                forward = False
            if event.key == pygame.K_s:
                backward = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            
            if event.key == pygame.K_f:
                f = False
    if forward == True:
        obj.scale += 2
    if backward == True:
        obj.scale -= 2
    if left == True:
        obj.angley += 0.001
        obj.pos[0] += 2
    if right == True:
        obj.pos[0] -= 2
        obj.angley -= 0.001

    if f == True:
        # obj.points.append(np.matrix([[randint(0, 10)], [randint(0, 10)], [randint(0, 10)]]))
        pass

    
    # obj.points[0] = [[-2], [-2], [2]]
    # obj.rotate(angle)
    obj.draw()
    obj.anglez += 0.01
    obj.angley += 0.01
    obj.anglex += 0.01
    
    # obj.scale -= 2

    pygame.display.update()

