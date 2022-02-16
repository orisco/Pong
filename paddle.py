from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.setx(position)
        self.sety(0)


    def move_up(self):
        y_cor = self.ycor()
        self.sety(y_cor + 20)


    def move_down(self):
        y_cor = self.ycor()
        self.sety(y_cor - 20)



