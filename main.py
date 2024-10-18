from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Lowen's Snake")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_square = Turtle("square")
    new_square.color("white")
    new_square.setpos(position)
    print(position)



screen.exitonclick()