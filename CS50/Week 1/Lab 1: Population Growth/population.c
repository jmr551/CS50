#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n, end_size, c = 0;

    // TODO: Prompt for start size
    int n = get_pop();

    // TODO: Prompt for end size
    end_size = get_int("End size: ");

    // TODO: Calculate number of years until we reach threshold
    while (n < end_size)
    {
        n = n + n/3 - n/4;
        c++;
    }

    // TODO: Print number of years
    printf("Years: %d\n",c);
}


int get_pop()
{
    int n = get_int("Start size: ");

    while (n < 9)
    {
        n = get_int("Please enter a number greater than or equal to 9: ");
    }

    return n;
}