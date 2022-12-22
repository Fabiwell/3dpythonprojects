from tkinter import *

window = Tk()
can = Canvas(window, width=900, height=900)

class block:
    def __init__(self, x, y, x2, y2, x3, y3, width, length, height, color):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.width = width
        self.length = length
        self.height = height
        self.color = color
        self.accel = 70
        self.scale = 1
        self.fov = 0.9
        self.yaw = 0.3
        self.pitch = 0.3
        self.oldx = 300
        self.oldy = 200

        self.points1 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.points2 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.points3 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.points4 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.points5 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.points6 = [0, 0, 0, 0, 0, 0, 0, 0]

        # self.middlex = window.winfo_width() / 2
        # self.middley = window.winfo_height() / 2
    def spawn(self):
        # x = self.x
        # y = self.y
        # width = self.width
        # height = self.height
        self.line1 = can.create_line(self.x, self.y, self.x + self.width, self.y, width=2)
        self.line2 = can.create_line(self.x, self.y, self.x, self.y + self.height, width=2)
        self.line3 = can.create_line(self.x + self.width, self.y, self.x + self.width, self.y + self.height, width=2)
        self.line4 = can.create_line(self.x, self.y + self.height, self.x + self.width, self.y + self.height, width=2)

        self.line5 = can.create_line(self.x, self.y, self.x + self.width, self.y, width=2)
        self.line6 = can.create_line(self.x, self.y, self.x, self.y + self.height, width=2)
        self.line7 = can.create_line(self.x + self.width, self.y, self.x + self.width, self.y + self.height, width=2)
        self.line8 = can.create_line(self.x, self.y + self.height, self.x + self.width, self.y + self.height, width=2)

        self.line9 = can.create_line(self.x, self.y, self.x + self.width, self.y, width=2)
        self.line10 = can.create_line(self.x, self.y, self.x, self.y + self.height, width=2)
        self.line11 = can.create_line(self.x + self.width, self.y, self.x + self.width, self.y + self.height, width=2)
        self.line12 = can.create_line(self.x, self.y + self.height, self.x + self.width, self.y + self.height, width=2)

        self.left = can.create_polygon(self.points2, fill=self.color)
        self.top = can.create_polygon(self.points3, fill=self.color)
        self.right = can.create_polygon(self.points1, fill=self.color)
        self.bottom = can.create_polygon(self.points4, fill=self.color)
        self.front = can.create_polygon(self.points5, fill=self.color)
        self.back = can.create_polygon(self.points6, fill=self.color)

    def update(self):
        x = window.winfo_pointerx()
        y = window.winfo_pointery()
        coords1 = can.coords(self.line1)
        coords5 = can.coords(self.line5)

        # if coords5[0] - coords1[0] < self.length:
        #     self.accel = 200
        #     print(self.accel)
        # else:
        #     self.accel = 70
        #     print(self.accel)

        can.move(self.line1, -((x - self.oldx) * self.fov), -((y - self.oldy) * self.fov))
        can.move(self.line2, -((x - self.oldx) * self.fov), -((y - self.oldy) * self.fov))
        can.move(self.line3, -((x - self.oldx) * self.fov), -((y - self.oldy) * self.fov))
        can.move(self.line4, -((x - self.oldx) * self.fov), -((y - self.oldy) * self.fov))

        can.move(self.line5, -((x - self.oldx) * (self.fov / 100 * 70)), -((y - self.oldy) * (self.fov / 100 * self.accel)))
        can.move(self.line6, -((x - self.oldx) * (self.fov / 100 * 70)), -((y - self.oldy) * (self.fov / 100 * self.accel)))
        can.move(self.line7, -((x - self.oldx) * (self.fov / 100 * 70)), -((y - self.oldy) * (self.fov / 100 * self.accel)))
        can.move(self.line8, -((x - self.oldx) * (self.fov / 100 * 70)), -((y - self.oldy) * (self.fov / 100 * self.accel)))

        coords1 = can.coords(self.line1)
        coords5 = can.coords(self.line5)

        can.coords(self.line9, coords1[0], coords1[1], coords5[0], coords5[1])
        can.coords(self.line10, coords1[0] + self.width, coords1[1], coords5[0] + self.width, coords5[1])
        can.coords(self.line11, coords1[0], coords1[1] + self.height, coords5[0], coords5[1] + self.height)
        can.coords(self.line12, coords1[0] + self.width, coords1[1] + self.height, coords5[0] + self.width, coords5[1] + self.height)

        self.points1 = [coords1[0], coords1[1], coords5[0], coords5[1], coords5[0], coords5[1] + self.height, coords1[0], coords1[1] + self.height]
        self.points2 = [coords1[0] + self.width, coords1[1], coords5[0] + self.width, coords5[1], coords5[0], coords5[1], coords1[0], coords1[1]]
        self.points3 = [coords1[0] + self.width, coords1[1], coords5[0] + self.width, coords5[1], coords5[0] + self.width, coords5[1] + self.height, coords1[0] + self.width, coords1[1] + self.height]
        self.points4 = [coords1[0], coords1[1] + self.height, coords5[0], coords5[1] + self.height, coords5[0] + self.width, coords5[1] + self.height, coords1[0] + self.width, coords1[1] + self.height]
        self.points5 = [coords1[0], coords1[1], coords1[0] + self.width, coords1[1], coords1[0] + self.width, coords1[1] + self.height, coords1[0], coords1[1] + self.height]
        self.points6 = [coords5[0], coords5[1], coords5[0] + self.width, coords5[1], coords5[0] + self.width, coords5[1] + self.height, coords5[0], coords5[1] + self.height]

        can.coords(self.left, self.points1)
        can.coords(self.top, self.points2)
        can.coords(self.right, self.points3)
        can.coords(self.bottom, self.points4)
        can.coords(self.back, self.points5)
        can.coords(self.front, self.points6)
        
        self.oldx = x
        self.oldy = y
        # print(can.coords(self.line1))
    def move(self, direction):
        if direction == 'forward':
            pass
        

        
        
    

# obj = block(200, 500, 200, 200, 100, 100, 600, 100, 300, 'blue')
# obj2 = block(200, 200, 200, 200, 100, 100, 50, 50, 50, 'white')
obj3 = block(500, 400, 200, 200, 100, 100, 100, 50, 100, 'brown')
# obj.spawn()
# obj2.spawn()
obj3.spawn()

def on_mouse_move(event):
    # block.update(obj)
    # block.update(obj2)
    block.update(obj3)


can.pack()
window.bind('<Motion>', on_mouse_move)
can.mainloop()


        