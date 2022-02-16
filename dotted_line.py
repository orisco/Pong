from turtle import Turtle


class DottedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, -300)
        self.setheading(90)
        self.color("white")
        self.hideturtle()
        self.create_line()

    def create_line(self):
        for i in range(20):
            self.forward(20)
            self.pu()
            self.forward(20)
            self.pd()