/*
Background
Say we have a population of n llamas. Each year, n / 3 new llamas are born, and n / 4 llamas pass away.

For example, if we were to start with n = 1200 llamas, then in the first year, 1200 / 3 = 400 new llamas
would be born and 1200 / 4 = 300 llamas would pass away. At the end of that year, we would have
1200 + 400 - 300 = 1300 llamas.

To try another example, if we were to start with n = 1000 llamas, at the end of the year, we would have
1000 / 3 = 333.33 new llamas. We can’t have a decimal portion of a llama, though, so we’ll truncate
the decimal to get 333 new llamas born. 1000 / 4 = 250 llamas will pass away, so we’ll end up with a
total of 1000 + 333 - 250 = 1083 llamas at the end of the year.
*/

#include <stdio.h>
#include <cs50.h>

int main()
{
    int n, end_size, c = 0;

    // Conditions
    n = get_int("Start size: ");
    end_size = get_int("End size: ");

    while (n < end_size)
    {
        n = n + n/3 - n/4;
        c++;
    }
    printf("Years: %d\n",c);

}