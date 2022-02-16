from turtle import Turtle

FONT = ('Arial', 100, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.update_score()

    def increase_score(self, player):
        if player == "l":
            self.l_score += 1
        elif player == "r":
            self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition((150, 200))
        self.write(f"{self.l_score}", align="left", font=FONT)
        self.setposition((-150, 200))
        self.write(f"{self.r_score}", align="right", font=FONT)
