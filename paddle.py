from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        x_corr = self.xcor()
        y_corr = self.ycor()
        if y_corr + 20 < 280:
            self.goto(x_corr, y_corr + 20)

    def down(self):
        x_corr = self.xcor()
        y_corr = self.ycor()
        if y_corr - 20 > -280:
            self.goto(x_corr, y_corr - 20)
