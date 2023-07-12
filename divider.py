from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=30, stretch_len=0.5)
