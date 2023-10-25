using System.Runtime.InteropServices;

class array_deque
{
    private string[] mass;
    private uint capacity;
    private uint length;

    public array_deque()
    {
        this.capacity = 0;
        this.length = 0;
    }

    public array_deque(ref uint size)
    {
        if (this.capacity != 0) { Console.WriteLine("error"); return; }
        this.mass = new string[size];
        this.capacity = size;
        this.length = 0;
    }

    public void print()
    {
        if(this.length == 0) { Console.WriteLine("empty"); return; }

        for(int i = 0; i < this.length; i++)
        {
            Console.Write(mass[i] + " ");
        }
        Console.WriteLine();
    }

    public void pushb(ref string elem)
    {
        if (this.capacity == this.length) { Console.WriteLine("overflow"); return; }

        this.mass[this.length] = elem;
        this.length++;
    }

    public void popb()
    {
        if(this.length == 0) { Console.WriteLine("underflow"); return; }

        this.mass[this.length - 1] = default;
        this.length--;
    }

    public void pushf(ref string elem)
    {
        if (this.capacity == this.length) { Console.WriteLine("overflow"); return; }

        for(uint i = this.length; i > 0; i--)
        {
            mass[i] = mass[i - 1];
        }
        this.mass[0] = elem;
        this.length++;
    }

    public void popf()
    {
        if (this.length == 0) { Console.WriteLine("underflow"); return; }

        for(int i = 0; i < this.length; i++)
        {
            this.mass[i] = this.mass[i+1];
        }
        this.mass[this.length] = default;
        this.length--;
    }
}

class Program
{
    static void Main()
    {
        array_deque deque = new array_deque();

        while (true)
        {
            string? input = Console.ReadLine(); if (input == null) { return; }

            input = input.Trim(); if (input == "") { continue; }

            var commands = input.Split(new char[] { ' ' }, 2);

            if (commands.Length == 1 && commands[0] == "print")
            {
                deque.print();
                continue;
            }
            else if(commands.Length == 1 && commands[0] != "print")
            {
                Console.WriteLine("error");
                continue;
            }

            if (commands[1].IndexOf(' ') != -1) { Console.WriteLine("error"); continue; }

            switch (commands[0])
            {
                case "set_size":
                    {
                        uint size = 0;
                        try
                        {
                            size = Convert.ToUInt32(commands[1]);
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine("error");
                            continue;
                        }

                        deque = new array_deque(ref size);
                        break;
                    }
                case "pushf":
                    {
                        deque.pushf(ref commands[1]);
                        break;
                    }
                case "pushb":
                    {
                        deque.pushb(ref commands[1]);
                        break;
                    }
                case "popf":
                    {
                        deque.popf();
                        break;
                    }
                case "popb":
                    {
                        deque.popb();
                        break;
                    }
                default:
                    {
                        Console.WriteLine("error");
                        break;
                    }
            }
        }

        //string input = Console.ReadLine();
        //Console.Write(input);
    }
}