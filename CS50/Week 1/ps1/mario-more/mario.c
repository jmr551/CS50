#include <cs50.h>
#include <stdio.h>

int get_height();

int main(void)
{
    int n;
    n = get_height();

    for (int i = 0; i < n; i++)
    {
        // This is for the first part
        for (int j = 0; j < n; j++)
        {
            if (j < n - i - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }

        printf("  ");

        // This is for the second part
        for (int j = 0; j < n; j++)
        {
            if (j < i + 1)
            {
                printf("#");
            }
        }

        printf("\n");
    }
}

int get_height()
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    return n;
}
