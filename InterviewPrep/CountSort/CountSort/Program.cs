using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CountSort
{
    class Program
    {
        static void Main(string[] args)
        {

            Random rnd = new Random();
            var inputArray = new int[20];

            for(int i = 0;i<20;i++)
            {
                inputArray[i] = rnd.Next(21);
            }

            CountSort(inputArray,20,0);


        }

        private static void CountSort(int[] inputArray, int maxValue,int minValue)
        {
            var trackCount = new Dictionary<int, int>();
            for (int i = 0; i < (maxValue-minValue+1); i++)
            {
                trackCount.Add(i, 0);
            }

            foreach (int num in inputArray)
            {
                trackCount[num]++;
            }
            var k = 0;
            for (int i = 0; i < (maxValue - minValue + 1); i++)
            {
                for(int j = 0;j< trackCount[i];j++)
                {
                    inputArray[k] = i;
                    k++;
                }
            }


        }
    }
}
