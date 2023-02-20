#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_height();

    for (int i = 0; i < n; i++)
    {
        // This is for the first part
        for (int j = 0; j<n; j++)
        {
            // ___# n=4,i=[0,3], i = 0, espacios = [0,3), # = [3,4)
            // caso 1: i=0, espacios = [0,1,2], n-i = 4-0 = 3, # = [3]
            if (j<n-i)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}

int get_height()
{
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    return n;
}