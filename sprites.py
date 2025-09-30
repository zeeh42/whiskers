from pathlib import Path
from tools import IO

class Tile:
    description=""
    walkable=False
    interactable=False
    def interact(self):
        pass # overwritten by inherrited tile
    def inspect(self):
        try:
            print(self.description)
        except NameError:
            print()

class Floor(Tile):
    description="it is the floor"
    walkable=True
    interactable=False

class Wall(Tile):
    description="a solid wall"
    walkable=False
    interactable=False

class Void(Tile):
    description="The void"
    walkable=False
    interactable=False

class Inventory:
    pointsTo=None

class Player:
    def __init__(self, x, y, maxHealth, inventory:Inventory):
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.inventory = inventory
        self.y = y
        self.x = x
    
    name=""

# used for translating text files into levels
key = {
    "T":Tile, # This should never be used
    "#":Wall,
    ".":Floor,
    " ":Void,
    "P":Player, # Used in printing the level
    "C":None, # TODO add Chest
    "S":None, # TODO add Stairs
    "D":None, # TODO add Door
}