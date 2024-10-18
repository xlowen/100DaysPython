from turtle import Screen
import time

class SnakeScreen:

    def __init__(self):

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Lowen's Snake")
        self.screen.tracer(0)
        self.update()
        self.screen.exitonclick()

    def update(self):
        self.screen.update()
        time.sleep(0.1)


