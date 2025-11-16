from turtle import Turtle

# Constants are often in all-caps to signify they shouldn't be changed.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Manages the snake's body, movement, and controls.
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial 3-segment snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the end of the snake (when it eats food)."""
        # Adds a segment at the same position as the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by one step."""
        # The segments follow the head.
        # Loop from the last segment to the second segment.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head (segment 0) forward.
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """Resets the snake to its original state after a game over."""
        # Move old segments off-screen before clearing
        for seg in self.segments:
            seg.goto(1000, 1000)  # Send them far away
        
        self.segments.clear()  # Empty the list
        self.create_snake()    # Create a new snake
        self.head = self.segments[0]

    # --- Control Methods ---
    # These methods prevent the snake from immediately reversing on itself.
    def up(self):
        """Sets snake's heading to UP (90) if not currently moving DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets snake's heading to DOWN (270) if not currently moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets snake's heading to LEFT (180) if not currently moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets snake's heading to RIGHT (0) if not currently moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)