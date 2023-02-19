#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n, end_size, c = 0;

    // TODO: Prompt for start size
    n = get_int("Start size: ");

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
