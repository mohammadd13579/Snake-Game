from turtle import Turtle

# Constants for styling and data
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")
DATA_FILE = "data.txt"

class Scoreboard(Turtle):
    """
    Manages the score display and high score persistence.
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)  # Position at the top center
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        """Loads the high score from the data file."""
        try:
            with open(DATA_FILE) as file:
                return int(file.read())  # Read the score and convert to int
        except (FileNotFoundError, ValueError):
            # If file doesn't exist or is empty/corrupt, return 0
            return 0

    def save_high_score(self):
        """Saves the current high score to the data file."""
        with open(DATA_FILE, mode="w") as file:
            file.write(str(self.high_score))  # Write the score as a string

    def update_scoreboard(self):
        """Clears the old score and writes the new score."""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increments the score and updates the display."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """
        Checks for a new high score, saves it, and resets the current score.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        
        self.score = 0  # Reset current score
        self.update_scoreboard()  # Update display to show Score: 0

    # Note: The original 'game_over' method is no longer needed,
    # as 'reset' handles the high score logic, and 'main.py'
    # restarts the game instead of stopping it.