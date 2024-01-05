from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    '''Creates a snake object with 3 starting segments'''
    def __init__(self):     
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        '''Moves snake forward by 20 pixels, starting from the tail'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        '''Moves snake up by 20 pixels'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        '''Moves snake up by 20 pixels'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Moves snake up by 20 pixels'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Moves snake up by 20 pixels'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        