from pathlib import Path

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

# used for translating text files into levels
key = {
    "T":Tile, # This should never be used
    "#":Wall,
    ".":Floor,
    " ":Void,
    "C":None, # TODO add Chest
    "S":None, # TODO add Stairs
    "D":None, # TODO add Door
}