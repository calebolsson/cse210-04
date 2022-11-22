from game.casting.actor import Actor

class Artifact(Actor):
    """A child of Actor, represents the discoverable elements on the map.

    The responsibility of Artifact(Actor) is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _message (string): The message to show when the Artifact is found

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
        self._message = ""

    def set_message(self, message):
        """Gets the artifact's display message.

        Args:
            message (string): The given value.
        """
        self._message = message

    def get_message(self):
        """Gets the artifact's display message.

        Returns:
            string: The artifact's display message.
        """
        return self._message
