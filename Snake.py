from turtle import Turtle

# constants
POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):

        for positions in POSITIONS:
            self.add_segment(positions)

    def add_segment(self,positions):
        Snake = Turtle(shape="square")
        Snake.color("white")
        Snake.penup()
        Snake.setposition(positions)
        self.segment.append(Snake)

    def extend(self):
        self.add_segment(POSITIONS[-1])

    def move_snake(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):  # start= len(segment),stop=0,step=-1
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
       if self.head.heading()!=DOWN:
         self.head.setheading(UP)
         self.move_snake()

    def down(self):
        if self.head.heading()!= UP:
         self.head.setheading(DOWN)
         self.move_snake()

    def right(self):
        if self.head.heading()!= LEFT:
         self.head.setheading(RIGHT)
         self.move_snake()

    def left(self):
        if self.head.heading()!=RIGHT:
             self.head.setheading(LEFT)
             self.move_snake()
