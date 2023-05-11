namespace ex1
{
    internal class Triangular : Tower
    {
        // Constructor that sets the width to 3 and height to input parameter
        public Triangular(int height, int width) : base(height, width)
        {
        }
        public override int Area()
        {
            return (Height * Width) / 2;
        }
        public override int Scope()
        {
            int x = (int)Math.Sqrt(Math.Pow(Height, 2) - Math.Pow(Width, 2));
            return x * 2 + Width;
        }
        public void print()
        {
            if (Width % 2 == 0 || (Height * 2) < Width)
            {
                Console.WriteLine("is is not possible to print the Triangular.");
            }
            else
            {
                string s = "";
                string s1 = " ";
                string s2 = "*";
                int counth = Height - 2;
                int w = Width - 2;
                int countw = 0;
                int num = 0;
                int numLast = 0;
                //counting on how many stars i can put in every line
                for (; w > 1; w -= 2, countw++) ;


                if (counth % countw == 0)
                {
                    num = 0;
                    numLast = counth / countw;
                }
                else
                {
                    int h = counth;
                    int i = 0;
                    for (i = 0; h % countw != 0; h--, i++) ;
                    num = h / countw;
                    numLast = num + i;
                }
                //number of starts that printed at this line
                int c = 1;
                s = "";
                int space = (Height - 1 - c) / 2;
                for (int j = 0; j < space; j++)
                {
                    s += s1;
                }
                for (int a = 0; a < c; a++)
                {
                    s += s2;
                }
                for (int j = 0; j < space; j++)
                {
                    s += s1;
                }
                Console.WriteLine(s);
                c += 2;
                for (int i = 1; i < Height + 1; i++)
                {
                    if (c == 3)
                    {
                        for (int z = 0; z < numLast; z++)
                        {
                            s = "";
                            space = (Height - 1 - c) / 2;
                            for (int j = 0; j < space; j++)
                            {
                                s += s1;
                            }
                            for (int a = 0; a < c; a++)
                            {
                                s += s2;
                            }
                            for (int j = 0; j < space; j++)
                            {
                                s += s1;
                            }
                            Console.WriteLine(s);
                            i++;

                        }
                    }
                    else
                    {
                        for (int z = 0; z < num; z++)
                        {
                            s = "";
                            space = (Height - 1 - c) / 2;
                            for (int j = 0; j < space; j++)
                            {
                                s += s1;
                            }
                            for (int a = 0; a < c; a++)
                            {
                                s += s2;
                            }
                            for (int j = 0; j < space; j++)
                            {
                                s += s1;
                            }
                            Console.WriteLine(s);
                            i++;
                        }
                    }
                    c += 2;
                }
                s = "";
                for (int a = 0; a < Width; a++)
                {
                    s += s2;
                }
                Console.WriteLine(s);
            }
        }
    }
}
