import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class object():
    def __init__(self, verticies):
        # self.x, self.y, self.z, self.x2, self.y2, self.z2 = x, y, z, x2, y2, z2
        self.verticies = verticies

        self.edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )

        self.surfaces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6),
        )

        self.colors = (
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (1, 1, 1)
            # (0, 1, 0),
            # (1, 1, 1),
            # (1, 1, 1),
            # (1, 1, 1),
            # (1, 1, 1),
            # (1, 1, 1),
            # (1, 1, 1)
        )

    def Cube(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            e = 0
            for vertex in surface:
                e+=1
                glColor3fv(self.colors[e])
                glVertex3fv(self.verticies[vertex])
        glEnd()
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])

        glEnd()
    
    def tesseract(self):
        self.x += 1

        self.verticies = (
            (self.x, self.y2, self.z2),
            (self.x, self.y, self.z2),
            (self.x2, self.y, self.z2),
            (self.x2, self.y2, self.z2),
            (self.x, self.y2, self.z),
            (self.x, self.y, self.z),
            (self.x2, self.y2, self.z),
            (self.x2, self.y, self.z)
        )



pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -5)

glRotatef(0, 0, 0, 0)
x1, y1, z1 = 1, -1, -1
x2, y2, z2 = 1, 1, -1
x3, y3, z3 = -1, 1, -1
x4, y4, z4 = -1, -1, -1
x5, y5, z5 = 1, -1, 1
x6, y6, z6 = 1, 1, 1
x7, y7, z7 = -1, -1, 1
x8, y8, z8 = -1, 1, 1
switch = True
switch2 = True
while True:
    verticies = (
        (x1, y1, z1),
        (x2, y2, z2),
        (x3, y3, z3),
        (x4, y4, z4),
        (x5, y5, z5),
        (x6, y6, z6),
        (x7, y7, z7),
        (x8, y8, z8)
    )
    # self.verticies = (
    #         (x, y2, z2),
    #         (x, y, z2),
    #         (x2, y, z2),
    #         (x2, y2, z2),
    #         (x, y2, z),
    #         (x, y, z),
    #         (x2, y2, z),
    #         (x2, y, z)
    #     )
    glRotatef(0.2, 0.3, 0.2, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                direction = 'left'
            if event.key == pygame.K_d:
                direction = 'right'
            if event.key == pygame.K_w:
                direction = 'forward'
            if event.key == pygame.K_s:
                direction = 'backward'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0, 0, 1)
            if event.button == 5:
                glTranslatef(0, 0, -1)
    obj = object(verticies)
    if x1 >= 0.5 and switch == True:
        x1 -= 0.01
        x2 -= 0.01
        x3 += 0.01
        x4 += 0.01
        y1 += 0.01
        y2 -= 0.01
        y3 -= 0.01
        y4 += 0.01
        z1 += 0.02
        z2 += 0.02
        z3 += 0.02
        z4 += 0.02

        z5 -= 0.02
        z6 -= 0.02
        z7 -= 0.02
        z8 -= 0.02
    elif x1 <= 1:
        switch = False
        x1 += 0.01
        x2 += 0.01
        x3 -= 0.01
        x4 -= 0.01
        y1 -= 0.01
        y2 += 0.01
        y3 += 0.01
        y4 -= 0.01

        z5 -= 0.02
        z6 -= 0.02
        z7 -= 0.02
        z8 -= 0.02

        z1 += 0.02
        z2 += 0.02
        z3 += 0.02
        z4 += 0.02
    elif x5 >= 0.5 and switch2 == True:
        x5 -= 0.01
        x6 -= 0.01
        x7 += 0.01
        x8 += 0.01
        y5 += 0.01
        y6 -= 0.01
        y7 += 0.01
        y8 -= 0.01

        z5 += 0.02
        z6 += 0.02
        z7 += 0.02
        z8 += 0.02

        z1 -= 0.02
        z2 -= 0.02
        z3 -= 0.02
        z4 -= 0.02
    elif x5 <= 1:
        switch2 = False
        x5 += 0.01
        x6 += 0.01
        x7 -= 0.01
        x8 -= 0.01
        y5 -= 0.01
        y6 += 0.01
        y7 -= 0.01
        y8 += 0.01

        z1 -= 0.02
        z2 -= 0.02
        z3 -= 0.02
        z4 -= 0.02

        z5 += 0.02
        z6 += 0.02
        z7 += 0.02
        z8 += 0.02
    else:
        switch = True
        switch2 = True

        



    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    obj.Cube()
    # obj.tesseract()
    pygame.display.flip()
    pygame.time.wait(10)
