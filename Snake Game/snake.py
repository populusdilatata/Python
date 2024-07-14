MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle

class Snake:
    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]

    def create_snake(self):
        # Create a snake body
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self, position):
        new_snake_block = Turtle(shape="square")
        new_snake_block.color("white")
        new_snake_block.penup()
        new_snake_block.goto(position)
        self.whole_snake.append(new_snake_block)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.whole_snake[-1].position())

    def move(self):
        # Tail will follow the head
        for new_snake_block_num in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[new_snake_block_num - 1].xcor()
            new_y = self.whole_snake[new_snake_block_num - 1].ycor()
            self.whole_snake[new_snake_block_num].goto(new_x, new_y)
            self.whole_snake[new_snake_block_num]
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
