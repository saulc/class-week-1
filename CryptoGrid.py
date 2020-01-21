


class CryptoGrid:
    #extra characters, fixed order.
    chars = [ "''", '(', ')', '*', '+', ',', '-', '.', '/'
    , ':', ';', '<', '>', '[', ']', '^', '?']

    grid = []
    listsize = 9
    mkey = ""

    def __init__(self):
        createGrid()

    def createGrid(self, key, message):
        self.grid = []
        mkey = key

    def encode(self, message):
        pass

    def decode(self, key):
        pass
