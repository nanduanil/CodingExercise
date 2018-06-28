using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pairs
{
    class Program
    {

        static int pairs(int k, int[] arr)
        {
            Array.Sort(arr);
            int countOfMatches = 0;
            int startCounter = arr.Length - 2;
            for(int i = arr.Length-1; i>=0; i--)
            {
                if(startCounter >= i) { startCounter = i - 1; }
                for (int j = startCounter; j >= 0; j--)
                {
                    var diff = arr[i] - arr[j];

                    if (diff > k)
                    { startCounter = j; break; }
                    else if(diff == k)
                    {
                        countOfMatches++;
                    }
                }
            }

            return countOfMatches;
        }


        static void Main(string[] args)
        {
            string[] nk = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nk[0]);

            int k = Convert.ToInt32(nk[1]);

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
            int result = pairs(k, arr);

            Console.WriteLine(result);
            
        }
    }
}
