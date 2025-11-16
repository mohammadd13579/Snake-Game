Python Snake Game
=================

A classic implementation of the Snake game built using Python's built-in Turtle module.

This project is a clean, object-oriented take on the retro arcade game. The goal is to eat the blue food, which makes the snake grow longer. Don't run into the walls or your own tail!

Features
--------

-   **Classic Gameplay:** Control the snake with the arrow keys.

-   **Score Tracking:** Your current score is displayed at the top.

-   **Persistent High Score:** The game saves your highest score to `data.txt`, so you can compete against yourself across multiple game sessions.

-   **Instant Reset:** When you lose, the game instantly resets, allowing for quick, "one-more-try" replayability.

-   **Clean, OOP Code:** The game is broken into logical classes (`Snake`, `Food`, `Scoreboard`) making it easy to read and maintain.

How to Run
----------

1.  Ensure you have Python 3 installed on your system.

2.  Clone or download this repository.

3.  Open a terminal or command prompt and navigate to the project directory.

4.  Run the main file:

    ```
    python main.py
    ```

Controls
--------

-   **Up Arrow:** Move snake up

-   **Down Arrow:** Move snake down

-   **Left Arrow:** Move snake left

-   **Right Arrow:** Move snake right

Project Structure
-----------------

-   `main.py`: The main game file. It initializes the screen, creates the game objects, and runs the main game loop.

-   `snake.py`: Contains the `Snake` class, which manages the snake's body, movement, and controls.

-   `food.py`: Contains the `Food` class, which controls the placement of the food pellet.

-   `scoreboard.py`: Contains the `Scoreboard` class, responsible for displaying the score and managing the high score data.

-   `data.txt`: (Will be created on first run) Stores the high score.