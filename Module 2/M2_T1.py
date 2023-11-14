import sys

class Splay_Tree:
    def __init__(self, key:int = None, value:str = None, parent = None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def min(self):
        min_elem = self
        stack = [min_elem.left, min_elem.right]

        while len(stack) != 0:
            elem = stack.pop(0)
            if elem is None: continue

            stack.append(elem.left)
            stack.append(elem.right)
            if elem.key < min_elem.key:
                min_elem = elem
        
        return min_elem

    def max(self):
        max_elem = self
        stack = [max_elem.left, max_elem.right]

        while len(stack) != 0:
            elem = stack.pop(0)
            if elem is None: continue

            stack.append(elem.left)
            stack.append(elem.right)
            if elem.key > max_elem.key:
                max_elem = elem
        
        return max_elem

    def print(self):
        pass

    def add(self, key, value):
        if self.key is None:
            self.key = key
            self.value = value
            return self
        
        current_elem = self
        while True:
            if key < current_elem.key:
                if current_elem.left is not None:
                    current_elem = current_elem.left
                    continue
                
                current_elem.left = Splay_Tree(key, value, current_elem)
                self = Splay_Tree.splay(self, current_elem.left)
                return self
            
            elif key > current_elem.key:
                if current_elem.right is not None:
                    current_elem = current_elem.right
                    continue

                current_elem.right = Splay_Tree(key, value, current_elem)
                self = Splay_Tree.splay(self, current_elem.right)
                return self
            
            else:
                print("error")
                return self

    def set(self, key, value):
        pass

    def remove(self, key):
        pass

    def search(self, key):
        pass

    def RotateLeft(self, elem):
        e_parent = elem.parent
        e_parent.right = elem.left

        if elem.left is not None:
            elem.left.parent = e_parent

        if e_parent.parent is None:
            self = elem
            self.parent = None
            self.left = e_parent
            e_parent.parent = self
            return self
        elif e_parent.parent.left == e_parent:
            e_parent.parent.left = elem
        else:
            e_parent.parent.right = elem

        elem.parent = e_parent.parent
        e_parent.parent = elem
        elem.left = e_parent
        return self

    def RotateRight(self, elem):
        e_parent = elem.parent
        e_parent.left = elem.right

        if elem.right is not None:
            elem.right.parent = e_parent
        
        if e_parent.parent is None:
            self = elem
            self.parent = None
            self.right = e_parent
            e_parent.parent = self
            return self
        elif e_parent.parent.left == e_parent:
            e_parent.parent.left = elem
        else:
            e_parent.parent.right = elem

        elem.parent = e_parent.parent
        elem.right = e_parent
        e_parent.parent = elem
        return self

    def ZigZigLeft(self, elem):
        self = Splay_Tree.RotateLeft(self, elem)
        self = Splay_Tree.RotateLeft(self, elem)
        return self

    def ZigZigRight(self, elem):
        self = Splay_Tree.RotateRight(self, elem)
        self = Splay_Tree.RotateRight(self, elem)
        return self

    def ZigZagLeft(self, elem):
        self = Splay_Tree.RotateLeft(self, elem)
        self = Splay_Tree.RotateRight(self, elem)
        return self

    def ZigZagRight(self, elem):
        self = Splay_Tree.RotateRight(self, elem)
        self = Splay_Tree.RotateLeft(self, elem)
        return self

    def splay(self, elem):
        while self.key != elem.key:
            if elem.parent == self:
                if self.left == elem:
                    self = Splay_Tree.RotateRight(self, elem)
                elif self.right == elem:
                    self = Splay_Tree.RotateLeft(self, elem)
                else:
                    print("error")
                    return
                
            elif (elem.parent.left == elem and elem.parent.parent.left == elem.parent):
                self = Splay_Tree.ZigZigRight(self, elem)
            elif (elem.parent.right == elem and elem.parent.parent.right == elem.parent):
                self = Splay_Tree.ZigZigLeft(self, elem)
            elif (elem.parent.left == elem and elem.parent.parent.right == elem.parent):
                self = Splay_Tree.ZigZagLeft(self, elem)
            elif (elem.parent.right == elem and elem.parent.parent.left == elem.parent):
                self = Splay_Tree.ZigZagRight(self, elem)
            else:
                print("error")
                return

        return self


ST = Splay_Tree()

for line in sys.stdin:
    line = line.strip('\n')

    if line == "" or line.find(" ") == 0: continue

    command, *args = line.split() 

    try:
        if len(args) == 0:
            match command:
                case "min":
                    min_elem = ST.min()
                    print("[ " + str(min_elem.key) + " " + str(min_elem.value) + " ]")
                case "max":
                    max_elem = ST.max()
                    print("[ " + str(max_elem.key) + " " + str(max_elem.value) + " ]")
                case "print":
                    ST.print()
                case _:
                    print("error")
        elif len(args) == 1:
            match command:
                case "search":
                    elem = ST.search(int(args[0]))
                    if elem is not None:
                        print("1 " + str(elem.value))
                    else:
                        print("0")
                case "delete":
                    ST.remove(int(args[0]))
                case _:
                    print("error")
        elif len(args) == 2:
            if (args[1].find(" ") != -1):
                print("error")
                continue
            match command:
                case "add":
                    ST = ST.add(int(args[0]), args[1])
                case "set":
                    ST = ST.set(int(args[0]), args[1])
                case _:
                    print("error")
        else:
            print("error")
    except ValueError:
        print("error")
    except:
        print("error")
