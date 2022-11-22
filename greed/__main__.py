import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.banner import Banner
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed: Minecraft Edition"
#DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Banner()
    banner.set_text(0)
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 100)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for n in range(MAX_X):
        floor = Actor()
        floor.set_text("_")
        robot.set_font_size(FONT_SIZE)
        robot.set_color(WHITE)
        floor.set_position(Point(n, y + FONT_SIZE))
        cast.add_actor("floor", floor)

    # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     gemvalues = data.splitlines()
    # NEW create the artifacts
    gemvalues = [100, -500, -10, 50, 10, 5]
    gemtext = ["E", "T", "S", "D", "G", "I"]
    gemcolors = [(0, 225, 0), (255, 0, 0), (155, 155, 155),
                 (0, 255, 255), (255, 255, 25), (255, 255, 255)]

    for n in range(DEFAULT_ARTIFACTS):
        # select value randomly from value array, include percent chance for rock
        # skin according to value and randomize starting location at max y range
        randindx = random.randrange(0, len(gemvalues))
        value = gemvalues[randindx]
        text = gemtext[randindx]
        color = Color(gemcolors[randindx][0],
                      gemcolors[randindx][1], gemcolors[randindx][2])
        x = random.randint(1, COLS - 1)
        y = random.randint(3, 7)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_value(value)
        artifact.set_velocity(Point(0, random.randrange(1, 10)))
        cast.add_actor("artifacts", artifact)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
