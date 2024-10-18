import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Lowen's Snake")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

squares = []
# def snake_speed(x):
#     speed = 0.5 - x
#     print(speed)
#
#     return time.sleep(speed)

# speed = 0

for position in starting_positions:
    new_square = Turtle("square")
    new_square.penup()
    new_square.color("white")
    new_square.setpos(position)
    squares.append(new_square)

game_is_on = True

while game_is_on:
    screen.update()


    for sqr_num in range(len(squares) - 1, 0, -1):
        new_x = squares[sqr_num - 1].xcor()
        new_y = squares[sqr_num - 1].ycor()
        squares[sqr_num].goto(new_x, new_y)
    squares[0].forward(20)


screen.exitonclick()