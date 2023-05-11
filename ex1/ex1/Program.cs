// See https://aka.ms/new-console-template for more information
using System;
using System.Runtime.CompilerServices;

namespace ex1
{
    internal class Program
    {
        static void Main()
        {
            Console.WriteLine("insert 1 for rectangle, 2 for triangle, 3 to exit");
            int x = Convert.ToInt32(Console.ReadLine()); 
            while (x != 3)
            {
                if (x == 1)
                {
                    Console.WriteLine("insert height Rectangle");
                    int h = Convert.ToInt32(Console.ReadLine());
                    while (h < 2)
                    {
                        Console.WriteLine("Height must be at least 2.");
                        Console.WriteLine("insert height Rectangle");
                        h = Convert.ToInt32(Console.ReadLine());
                    }
                    Console.WriteLine("insert width Rectangle");
                    int w = Convert.ToInt32(Console.ReadLine()); 
                    
                    // Create a Rectangle tower
                    Rectangle r = new Rectangle(w,h);
                }
                else if (x == 2) 
                {
                    Console.WriteLine("insert height triangle");
                    int h = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine("insert width triangle");
                    int w = Convert.ToInt32(Console.ReadLine());
                    if (h < 2)
                    {
                        Console.WriteLine("Height must be 2.");
                        Console.WriteLine("insert height triangle");
                        h = Convert.ToInt32(Console.ReadLine());
                    }
                    // Create a Triangular tower
                    Triangular t = new Triangular(h, w );
                    Console.WriteLine("insert 1 for scope, 2 for printing");
                    int y = Convert.ToInt32(Console.ReadLine());
                    if (y == 1)
                    {
                        Console.WriteLine(t.Scope());
                    }
                    else { t.print() ; }
                }
                else
                {
                    Console.WriteLine("you can insert only 1,2 or 3");
                }
                Console.WriteLine("insert 1 for rectangle, 2 for triangle, 3 to exit");
                x = Convert.ToInt32(Console.ReadLine());
            }

        }

    }
}
