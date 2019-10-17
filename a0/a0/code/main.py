"""
This module loads, configures and runs the main game.
"""

from game import Game
from actors import *
from typing import List
import random


def load_map(filename: str) -> List[List[str]]:
    """
    Load the map data from the given filename and return as a list of lists.
    """

    with open(filename) as f:
        map_data = [line.split() for line in f]
    return map_data


if __name__ == "__main__":

    data = load_map("../data/maze0.txt") # Set the filename where maze data is

    width = len(data[0])
    height = len(data)

    game = Game(width, height)
    player, chaser = None, None

    # Loops through the rows and columns of maze0.txt and has a variable called
    # key which stores the letter at given index of row and column through each
    # iteration of the loop. This 'key' is then compared to check if it is a
    # 'P', 'C' or 'X'. If it is a 'P' then a Player instance is created
    # and assigned to the player variable which will be the player of
    # the game, if it is a 'C' then a Chaser instance is created and assigned to
    # the chaser variable which will be the ghost in the game and if it is a 'X'
    #  then a Wall instance is created and added to the list of characters
    # within the game.
    for i in range(len(data)):
        for j in range(len(data[i])):
            key = data[i][j]
            if key == 'P':
                player = Player("../images/boy-24.png", j, i)
            elif key == 'C':
                chaser = Chaser("../images/ghost-24.png", j, i)
            elif key == 'X':
                game.add_actor(Wall("../images/wall-24.png", j, i))

    game.set_player(player)
    game.add_actor(player)
    game.add_actor(chaser)
    # Set the number of stars the player must collect to win
    game.goal_stars = 5

    # The purpose of this loop is to create 8 randomly located stars. This is
    # done with the help of the variables x, y which pick random nums
    # (coordinates) within the boundaries of the width and height of the game
    # respectively. The x and y variables are changed through each iteration of
    # the loop so stars do not spawn on each other. Furthermore, a star object
    # is created each iteration of the loop with the randomly generated x, y
    # integers and added to the game class
    num_stars = 0
    while num_stars < 8:
        x = random.randrange(game.stage_width)
        y = random.randrange(game.stage_height)

        if not game.get_actor(x, y):
            game.add_actor(Star("../images/star-24.png", x, y))
            num_stars += 1

    game.on_execute()
