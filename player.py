from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)
        # self.goto(STARTING_POSITION)
        self.start_line()

    def move(self):
        # y = self.ycor() + 10
        self.forward(MOVE_DISTANCE)
        # self.goto(0, y)

    def start_line(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

