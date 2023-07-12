from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")
GO_FONT = ("Ariel", 30, "normal")
WIN_FONT = ("Ariel", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self, side):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(f"{side} paddle wins", move=False, align=ALIGNMENT, font=WIN_FONT)
