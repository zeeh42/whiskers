import os
import config as C
from pathlib import Path

class IO:

    @staticmethod
    def keyToValueDict(dict):
        """returns a list where all the values are the keys"""
        newDict = {v: k for k, v in dict.items()}
        return newDict

class Title:
    """text to ascii class"""

    # Do not use default font
    fonts = {} # fonts = {"fontname":{"a":["  __  ", " / _\ ", "/    \\", "\_/\_/"]}}

    @staticmethod
    def getTitle(text, fontname,):
        """returns an ascii banner as a string"""
        font = Title.fonts[fontname]

        # TODO return a banner as a string from the font and the text, i wasted time trying to do this...

        return "TODO: get title as string"

    @staticmethod
    def loadFont(fontname):
        """add a font to Title.fonts"""
        fontPath = C.Path.FONTDIRPATH / Path(fontname) 

        newFont = {}

        for letterfile in os.listdir(fontPath):
            filePath = fontPath / Path(letterfile)
            with open(filePath) as f:
                lines = [line.replace("\n", "") for line in f.readlines()] # Remove new line character
                newFont.update({letterfile:lines})
        Title.fonts.update({fontname:newFont})

    @staticmethod
    def removeFont(fontname):
        """Removes a font from Title.fonts"""
        try:
            Title.fonts.pop(fontname)
        except KeyError:
            raise KeyError(f"{fontname} is not a font")