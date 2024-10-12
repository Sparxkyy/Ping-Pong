from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1, 1)

        self.goto(0,0)
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1
        self.move_speed*=0.9

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def score_board(self):


        self.write(f"game over, your score:", align="center", font=18)
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()




