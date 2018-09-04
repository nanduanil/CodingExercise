using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IsBST
{
    class Program
    {
        static void Main(string[] args)
        {
            int k = 5;

            Queue<int> q = new Queue<int>(new int[] { 10, 20, 30, 40, 50, 60, 70, 80, 90 });

            q = rotateQueue(q);


        }

        static Queue<int> rotateQueue(Queue<int> q)
        {
            Stack<int> s = new Stack<int>();

            for (int i = 0; i < k; i++)
            {
                s.Push(q.Dequeue());
            }

            int count = q.Count;

            while (s.Count > 0)
            {
                q.Enqueue(s.Pop());
            }

            for (int i = 0; i < count; i++)
            {
                q.Enqueue(q.Dequeue());
            }

            return q;

        }

    }
}
