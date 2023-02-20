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
            // ___# n=4, i=[0,3], espacios = []
            if ()
            {

            }
            else
            {

            }

        }
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