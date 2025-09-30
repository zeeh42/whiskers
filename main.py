import config as C
import sprites as S
from tools import *
from pathlib import Path

class level:
    def __init__(self):
        self.outOfIndexTile = S.Void()

    level = []

    def loadLevel(self, levelPath:Path):
        if levelPath.suffix != ".level":
            raise FileNotFoundError(f"Wrong file type for level, {levelPath} needs to end with .level")
        newLevel = []
        with open(levelPath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                x = []
                for char in line.replace("\n", ""):
                    x.append(S.key[char]())
                newLevel.append(x)
        self.level = newLevel

    def getTile(self, x, y, level=level):
        try:
            return level[y][x]
        except IndexError:
            return self.outOfIndexTile
    
    def setTile(self, x, y, level, Tile):
        # Tile doesn't have a specfic type because it is also used in getLevelAsPrint()
        newLevel = level
        try:
            newLevel[y][x] = Tile
            return newLevel
        except IndexError:
            raise IndexError(f"Tile {x}, {y} is out of this world!")
            

    def getLevelAsPrint(self, player):
        printLevel = self.level
        printLevel = self.setTile(player.x, player.y, printLevel, player)

        stringToReturn = ""
        for i, line in enumerate(printLevel):
            for tile in line:
                stringToReturn += IO.keyToValueDict(S.key)[tile.__class__] # get the char from the tiletype
            if i != (len(printLevel)-1): # only add newline if not lastline
                stringToReturn += "\n"
        return stringToReturn

level = level()
player = S.Player(x=1, y=1, maxHealth=100, inventory=None)
level.loadLevel(Path("level/test.level"))
print(level.getLevelAsPrint(player))