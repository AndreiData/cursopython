using System;

public class Program
{
    public static void Main()
    {
        int[] numero = new int[5];
        int suma;
        int i;

        for (i = 0; i <= 4; i++)
        {
            Console.WriteLine("Introduce el dato numero {0}: ", i + 1);
            numero[i] = Convert.ToInt32(Console.ReadLine());
        }

        suma = 0;
        for (i = 0; i <= 4; i++)
            suma += numero[i];

        Console.WriteLine("Su suma es: {0}", suma);
    }
}
