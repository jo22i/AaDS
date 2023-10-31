import sys

class array_deque:
    # Инициализация первоначального размера дэка для удобства детектирования
    # попыток его повторной инициализации
    capacity = 0
    nullable = False

    def __init__(self, size: int):
        # Проверка длины на неотрицательность и нуль
        if (size < 0):
            print("error")
            return
        elif (size == 0): self.nullable = True
        
        # Установка размера дэка
        self.mass = [""]*size
        # Установка переменной с размером дэка
        self.capacity = size
        # Установка переменной с кол-вом записанных ячеек
        self.length = 0
        # Установка указателей на первый и последний элемент дэка
        # Так как дэк новый, то указатели одинаковые и указывают на единственный
        # пока ещё не появившийся первый элемент
        # В данном случае было решено поставить первый элемент в начало массива
        self.head = self.tail = 0

    def print(self):
        # Проверка на пустоту и возможный вызов функции при отсутствии инициализации дэка
        if (self.capacity == 0 and not self.nullable):
            print("error")
            return
        elif (self.length == 0):
            print("empty")
            return

        # Если элемент всего один, то он и печатается
        if (self.length == 1):
            print(self.mass[self.head])
            return

        # Иначе перебираем все элементы дека, начиная с начального указателя 
        # и до последнего доступного элемента
        answer = ""
        index = self.head
        while (index != self.tail):
            answer += self.mass[index] + " "

            if (index == len(self.mass) - 1):
                index = 0
                continue
            
            index += 1
        else:
            # Перехват последнего элемента
            answer += self.mass[index]
        
        # Вывод всех элементов
        print(answer.rstrip())

    def pushf(self, elem: str):
        # Проверка на переполнение и возможный вызов функции при отсутствии инициализации дэка
        if (self.capacity == 0 and not self.nullable):
            print("error")
            return
        elif (self.capacity == self.length):
            print("overflow")
            return
        
        # Если дэк пуст, то добавляемый элемент - первый, ставится в начало
        if (self.length == 0):
            self.mass[self.head] = elem
            self.length += 1
            return
        
        # Иначе ставим его первым элементом в списке и переcтавляем на него указатель head
        self.length += 1
        self.head = (self.capacity - 1) if (self.head == 0) else (self.head - 1)
        self.mass[self.head] = elem

    def pushb(self, elem: str):
        # Проверка на переполнение и возможный вызов функции при отсутствии инициализации дэка
        if (self.capacity == 0 and not self.nullable):
            print("error")
            return
        elif (self.capacity == self.length):
            print("overflow")
            return
        
        # Если дэк пуст, то добавляемый элемент - первый, ставится в начало
        if (self.length == 0):
            self.mass[self.head] = elem
            self.length += 1
            return

        # Иначе ставим его на следующее место после tail и меняем указатель tail на него
        self.length += 1
        self.tail = (0) if (self.tail == self.capacity - 1) else (self.tail + 1)
        self.mass[self.tail] = elem
        
    def popb(self):
        # Проверка на пустоту и возможный вызов функции при отсутствии инициализации дэка
        if (self.capacity == 0 and not self.nullable):
            print("error")
            return
        elif (self.length == 0):
            print("underflow")
            return
        
        # Уменьшаем длину списка на 1 элемент
        self.length -= 1
        
        # Если там был всего один элемент - его и выводим, он на указателях head и tail
        if (self.length == 0):
            print(self.mass[self.head])
            return

        # Иначе берём его по указателю tail и сдвигаем указатель
        answer, self.mass[self.tail] = self.mass[self.tail], ""
        self.tail = (self.capacity - 1) if (self.tail == 0) else (self.tail - 1)

        # Возврат элемента
        return answer

    def popf(self):
        # Проверка на пустоту и возможный вызов функции при отсутствии инициализации дэка
        if (self.capacity == 0 and not self.nullable):
            print("error")
            return
        elif (self.length == 0):
            print("underflow")
            return
        
        # Уменьшаем длину списка на 1 элемент
        self.length -= 1

        # Если там был всего один элемент - его и выводим, он на указателях head и tail
        if (self.length == 0):
            print(self.mass[self.head])
            return
        
        # Иначе берём его по указателю head и сдвигаем указатель
        answer, self.mass[self.head] = self.mass[self.head], ""
        self.head = (0) if (self.head == self.capacity - 1) else (self.head + 1)

        # Возврат полученного элемента
        return answer

# Инициализация пустого дэка и переменной для получения команд из командной строки
Deque = array_deque
# Цикл обработки команд из командной строки
for line in sys.stdin: 
    try:
        line = line.rstrip('\n')
        # Пропуск пустых строк
        if (line == "" or line == '\n'):
            continue

        # Получение списка команд с помощью разбиения строки по разделительному пробелу
        commands = line.split(" ", 1)

        # Проверка на кол-во команд
        # Одна строка - 3 возможные команды: popf, popb, print
        # Иначе получается 2 строки и соответственно 3 другие команды: set_size, pushf, pushb
        # Если есть несоответствие 3 вышеперечисленным командам - выводим ошибку
        if (len(commands) == 1):
            match commands[0]:
                case "print":
                    Deque.print()
                    continue
                case "popf":
                    answer = Deque.popf()
                    if (answer): print(answer)
                    continue
                case "popb":
                    answer = Deque.popb()
                    if (answer): print(answer)
                    continue
                case _:
                    print("error")
                    continue

        # Если нашли лишние пробелы во второй строке для команд - значит он лишний
        # и необходимо вывести сообщение об ошибке
        if (commands[1].find(" ") != -1 or commands[1] == ""):
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
        # Если при получении команды set_size во втором агрументе было не целое число,
        # то вызывается ValueError, который мы ловим и выводим собщение об ошибке
        except ValueError:
            print("error")
            continue
        except:
            print("error")
            continue
    # Данный тип ошибки возникнет при окончании ввода с консоли, 
    # который означает завершение программы
    except:
        print("error")
        continue