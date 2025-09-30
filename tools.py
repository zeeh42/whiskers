
class IO:

    @staticmethod
    def keyToValueDict(dict):
        newDict = {v: k for k, v in dict.items()}
        return newDict