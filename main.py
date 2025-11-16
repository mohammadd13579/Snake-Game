from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# The wall boundary is half the screen width/height, minus the size of one snake segment (20px)
# This prevents the snake head from partially disappearing before the game over.
WALL_LIMIT = (SCREEN_WIDTH // 2) - 20 

# --- Screen Setup ---
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# --- Game Object Initialization ---
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- Keyboard Bindings ---
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- Main Game Loop ---
game_is_on = True
while game_is_on:
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Control game speed
    snake.move()

    # 1. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 2. Detect collision with wall
    if (snake.head.xcor() > WALL_LIMIT or snake.head.xcor() < -WALL_LIMIT or
            snake.head.ycor() > WALL_LIMIT or snake.head.ycor() < -WALL_LIMIT):
        scoreboard.reset()  # Reset score and check for high score
        snake.reset()       # Reset snake to starting position

    # 3. Detect collision with tail
    # Slicing the list [1:] ignores the head (index 0)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()