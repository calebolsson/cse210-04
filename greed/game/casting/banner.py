from game.casting.actor import Actor

class Banner(Actor):
    """A child of Actor, used as a display and scorekeeping element.

    The responsibility of Banner(Actor) is to keep score and display score updates.

    Attributes:
        _max_score (int): The highest score achieved in this run
        _score (int): The current score in this run
        _points (int): The last point value that modified the score

    Inherited Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._max_score = 0
        self._score = 0
        self._points = 0

    def set_text(self, value):
        """Updates the banner's score values.

        Args:
            value (int): The points that are modifying the score.
        """
        self._points = value
        self._score += value
        if self._score > self._max_score:
            self._max_score = self._score
        self._text = "Max_Score: " + str(self._max_score) + "\nScore: " + str(self._score) + " (" + str(self._points) + ")"

    def get_text(self):
        """Gets the artifact's score value.

        Returns:
            int: The artifact's score value.
        """
        return self._text

    def positive_score(self):
        """Checks if the player still has a positive score
        
        Returns:
            bool: True if score >= 0.
        """
        if self._score >= 0:
            return True
        return False