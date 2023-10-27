class array_deque:
    capacity = 0

    def __init__(self, size):
        if(size <= 0):
            print("error")
            return
        
        self.mass = [""]*size
        self.capacity = size
        self.length = 0

        self.head = self.tail = 0

    def print(self):
        if(self.length == 0):
            print("empty")
            return
        elif(self.capacity == 0):
            print("error")
            return

        if (self.length == 1):
            print(self.mass[self.head])
            return

        answer = ""
        index = self.head
        while (index != self.tail + 1):
            if (index == len(self.mass)):
                index = 0
            answer += (self.mass[index] + " ") if (self.mass[index] != "") else ""
            index += 1
        
        print(answer.rstrip())

    def pushf(self, elem):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.capacity == self.length):
            print("overflow")
            return
        
        if (self.length == 0):
            self.mass[self.head] = elem
            self.length += 1
            return
        
        self.length += 1

        self.head = (self.capacity - 1) if (self.head == 0) else (self.head - 1)
        
        self.mass[self.head] = elem

    def pushb(self, elem):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.capacity == self.length):
            print("overflow")
            return
        
        if (self.length == 0):
            self.mass[self.head] = elem
            self.length += 1
            return

        self.length += 1

        self.tail = (0) if (self.tail == self.capacity - 1) else (self.tail + 1)

        self.mass[self.tail] = elem
        
    def popb(self):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.length == 0):
            print("underflow")
            return
        
        self.length -= 1
        
        if (self.length == 0):
            print(self.mass[self.head])
            return

        print(self.mass[self.tail])

        self.tail = (self.capacity - 1) if (self.tail == 0) else (self.tail - 1)

    def popf(self):
        if(self.capacity == 0):
            print("error")
            return
        elif(self.length == 0):
            print("underflow")
            return

        self.length -= 1

        if (self.length == 0):
            print(self.mass[self.head])
            return
        
        print(self.mass[self.head])

        self.head += 1
        if (self.head == self.capacity): self.head = 0

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