from turtle import Turtle
from food import Food

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_POSITION = 20
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
        for position in START_POS:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)

    def reset(self):
        for segments in self.segment:
            segments.goto(2000,2000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
            for i in range(len(self.segment)-1, 0, -1):
                x = self.segment[i - 1].xcor()
                y = self.segment[i - 1].ycor()
                self.segment[i].goto(x, y)
            self.head.forward(MOVE_POSITION)

    def c_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def c_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def c_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def c_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def wall_collide(self):
        a=self.head.xcor()
        b=self.head.ycor()
        if a<-280 or a>280 or b<-280 or b>280:
            return True
        else:
            return False

    def snake_collide(self):
        flag = 0
        for seg in range(len(self.segment)-1, 2, -1):
            if self.head.distance(self.segment[seg]) < 20:
                flag = 1
        if flag == 1:
            return True
        else:
            return False

