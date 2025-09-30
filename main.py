import config as C
import sprites as S
from pathlib import Path

class level:
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

level = level()
level.loadLevel(Path("level/test.level"))
for line in level.level:
    print(line)