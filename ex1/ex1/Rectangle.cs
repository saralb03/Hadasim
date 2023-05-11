using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex1
{
    internal class Rectangle : Tower
    {
        public Rectangle(int height, int width) : base(height, width)
        {
            if (height == width || Math.Abs(height - width) > 5)
            {
                Console.WriteLine(Area());
            }
            else
            {
                Console.WriteLine(Scope());
            }
        }
        public override int Scope() { return Height * 2 + Width * 2; }
        public override int Area() { return Height * Width; }

    }
}
