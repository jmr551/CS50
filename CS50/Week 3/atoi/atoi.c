#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    int n;

    if (strlen(input)==0)
    {
        return 0;
    }
    else
    {
        n = input[strlen(input)-1] - '0';
        input[strlen(input)-1] = '\0';
        return n + 10 * convert(input);

    }
}



/*
input = '12345'

convert('12345')
n =


*/