from turtle import Turtle
import random

# Adjusted range to be within the 280 wall limit, giving a 10px buffer
FOOD_SPAWN_RANGE = 270

class Food(Turtle):
    """
    Manages the food item for the snake.
    Inherits from Turtle, so it *is* a Turtle object.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 pixels
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food to a new random position on the screen."""
        random_x = random.randint(-FOOD_SPAWN_RANGE, FOOD_SPAWN_RANGE)
        random_y = random.randint(-FOOD_SPAWN_RANGE, FOOD_SPAWN_RANGE)
        self.goto(random_x, random_y)