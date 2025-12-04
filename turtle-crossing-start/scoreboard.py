from turtle import Turtle
FONT = ("Courier", 24, "normal")
score = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)
        self.level += 1


