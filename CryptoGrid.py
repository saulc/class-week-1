


class CryptoGrid:
    #extra characters, fixed order.
    chars = [ "''", '(', ')', '*', '+', ',', '-', '.', '/'
    , ':', ';', '<', '>', '[', ']', '^', '?']

    grid = []
    listsize = 9
    mkey = ""

    def __init__(self, key, message):
        self.createGrid(key, message)

    def createGrid(self, key, message):
        self.grid = []
        self.mkey = key
        for i in range(0, self.listsize*self.listsize):
            self.grid.append(str(i))

    def encode(self, message):
        pass

    def decode(self, key):
        pass

    def printGrid(self):
        prt = ""
        k = 0
        for i in self.grid:
            prt += i + " "
            k += 1
            end = ( ( k % self.listsize) == 0 )
            if( end ):
                print(prt)
                prt = ""

def testGrid():
    msg = "hello"
    key = "test key"
    gd = CryptoGrid(key, msg)
    gd.printGrid()

if __name__ == "__main__":
    testGrid()
