# Grid Class
import string

class CryptoGrid:
    #extra characters, fixed order.
    extra_chars = [ "''", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '>', '[', ']', '^', '?']

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    grid_size = 9

    def __init__(self):
        self.mkey = self.get_input()
        self.grid = self.createGrid()


    def createGrid(self):
        # print("in grid")
        leftover = ""
        upper_leftover = [x for x in self.upper if x not in self.mkey]
        lower_leftover = [x for x in self.lower if x not in self.mkey]
        extra_leftover = [x for x in self.extra_chars if x not in self.mkey]
        leftover = self.mkey + upper_leftover + lower_leftover + extra_leftover
        # print(leftover)
        return leftover

    def get_input(self):
        raw_input = input("Enter key: ")
        split_input_list = raw_input.split('"')
        action = split_input_list[0]
        code_word = split_input_list[1]
        message = split_input_list[3]

        if(action == 'encode '):
            print("encode")
        elif (action == 'decode '):
            print("decode")
        else:
            print("bad input")

        key_dict = dict()
        # Clean input
        order = 0;
        for char in code_word:
            if char not in key_dict:
                key_dict[char] = order
                order += 1              # holds the order
        # print(key_dict.keys())
        key_list = []
        for key in key_dict.keys():
            key_list.append(key)
        return key_list

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
