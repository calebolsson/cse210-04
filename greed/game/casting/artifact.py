from game.casting.actor import Actor

class Artifact(Actor):
    """A child of Actor, represents the collectable elements on the map.

    The responsibility of Artifact(Actor) is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _value (int): The score value of the gem/rock

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
        self._value = 0

    def set_value(self, value):
        """Sets the artifact's score value.

        Args:
            value (int): The artifact's score value.
        """
        self._value = value

    def get_value(self):
        """Gets the artifact's score value.

        Returns:
            int: The artifact's score value.
        """
        return self._value

    def passed_over(self,target_x,target_y):
        """Indicates if the artifact has passed over a target.
        
        Returns:
            bool: If the target was passed over.
        """
        if target_x == super().get_position().get_x():
            if target_y == super().get_position().get_y():
                return True
            elif target_y < super().get_position().get_y() and target_y > super().get_position().get_y() - super().get_velocity().get_y():
                return True
        return False