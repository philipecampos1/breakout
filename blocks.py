from turtle import Turtle


class Blocks(Turtle):
    def __init__(self, position_x, position_y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(x=position_x,y=position_y)

    def destroy(self):
        self.goto(1000,1000)



