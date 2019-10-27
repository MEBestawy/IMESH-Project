import pygame
from GameObject import GameObject
from typing import List


class Handler:
    """
    This class handles the animation and the rendering
    of the game objects in the main game.

    ===Private Attributes===

    _objects: A list of all game objects in the main game

    """
    # Private Attributes
    _objects: List[GameObject]

    def __init__(self):
        """
        Initializes an empty list of game objects.
        """
        self._objects = []

    def tick(self):
        """
        Animates each game object in _objects.
        """
        for obj in self._objects:
            obj.tick()

    def render(self, display: pygame.Surface):
        """
        Renders each game object in _objects.
        """
        for obj in self._objects:
            obj.render(display)

    def add_object(self, obj: GameObject):
        """
        Adds a game object to the _objects.
        """
        self._objects.append(obj)

    def remove_object(self, obj: GameObject):
        """
        Removes a specified game object in _objects.
        """
        self._objects.remove(obj)

    def clear_all(self):
        """
        Removes all game objects in _objects.
        """
        for obj in self._objects:
            self.remove_object(obj)
