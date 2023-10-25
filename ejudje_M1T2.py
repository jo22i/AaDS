class array_deque:
    mass = []
    capacity = 0
    length = 0

    def __init__(self, size):
        if(size <= 0):
            print("error")
            return
        
        self.mass = [""]*size
        self.capacity = size
        self.length = 0

    def print(self):
        if(self.length == 0):
            print("empty")
            return
        elif(self.capacity == 0):
            print("error")
            return

        print(" ".join(self.mass).rstrip())

    def pushf(self, elem):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.capacity == self.length):
            print("overflow")
            return
        
        for i in range(self.length, 0, -1):
            self.mass[i] = self.mass[i-1]

        self.mass[0] = elem
        self.length += 1

    def pushb(self, elem):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.capacity == self.length):
            print("overflow")
            return
        
        self.mass[self.length] = elem
        self.length += 1
        
    def popb(self):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.length == 0):
            print("underflow")
            return
        
        print(self.mass[self.length-1])
        
        self.mass[self.length-1] = ""
        self.length -= 1

    def popf(self):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.length == 0):
            print("underflow")
            return
        
        print(self.mass[0])
        
        for i in range(0, self.length-1):
            self.mass[i] = self.mass[i+1]
        
        self.mass[self.length-1] = ""
        self.length -= 1

Deque = array_deque

line = ""

while(True):
    try:
        line = input()
        if(line == ""):
            continue

        commands = line.split(" ", 1)

        if(len(commands) == 1):
            match commands[0]:
                case "print":
                    Deque.print()
                    continue
                case "popf":
                    Deque.popf()
                    continue
                case "popb":
                    Deque.popb()
                    continue
                case _:
                    print("error")
                    continue

        if(commands[1].find(" ") != -1 or commands[1] == ""):
            print("error")
            continue
        
        try:
            match commands[0]:
                case "set_size":
                    if(Deque.capacity == 0):
                        Deque = array_deque(int(commands[1]))
                    else:
                        print("error")
                case "pushb":
                    Deque.pushb(str(commands[1]))
                case "pushf":
                    Deque.pushf(str(commands[1]))
                case _:
                    print("error")
            continue
        except ValueError:
            print("error")
            continue
        except:
            print("error")
            continue

    except EOFError:
        break
    except:
        print("error")
        continue