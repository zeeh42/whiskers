import os
import config as C
from pathlib import Path

class IO:

    @staticmethod
    def keyToValueDict(dict):
        newDict = {v: k for k, v in dict.items()}
        return newDict

class Title:

    # Do not use default font
    fonts = {} # fonts = {"fontname":{"a":["  __  ", " / _\ ", "/    \\", "\_/\_/"]}}

    @staticmethod
    def getTitle(fontname):
        font = Title.fonts[fontname]
        string = ""
        
        

    @staticmethod
    def loadFont(fontname):
        fontPath = C.Path.FONTDIRPATH / Path(fontname) 

        newFont = {}

        for letterfile in os.listdir(fontPath):
            filePath = fontPath / Path(letterfile)
            with open(filePath) as f:
                lines = [line.replace("\n", "") for line in f.readlines()] # Remove new line character
                newFont.update({letterfile:lines})
        Title.fonts.update({fontname:newFont})


    def removeFont(fontname):
        try:
            Title.fonts.pop(fontname)
        except KeyError:
            raise KeyError(f"{fontname} is not a font")

Title.loadFont("mavic")
print(Title.fonts["mavic"])