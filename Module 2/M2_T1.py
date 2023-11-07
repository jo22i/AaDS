import sys

class Slpay_Tree:
    def __init__(self, key : int, value : str):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.rigth = None

    def add(self, key, value):
        pass

    def remove(self, key):
        pass

    def remove(self, value):
        pass

    def search(self, key):
        pass
    
    def search(self, value):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def print(self):
        pass


def RotateLeft():
    pass

def RotateRigth():
    pass

def ZigZig():
    pass

def ZigZag():
    pass

def splay(Tree, X):
    pass


ST = Slpay_Tree()

for line in sys.stdin:
    line = line.strip('\n')

    if line == "" or line.find(" ") == 0: continue

    command, *args = line.split() 
    if len(args) == 0:
        match command:
            case "min":
                ST.min()
            case "max":
                ST.max()
            case "print":
                ST.print()
            case _:
                print("error")
    else:
        if len(args) != 2
        match command:
            case "":
                pass
            case _:
                print("error")
