#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool validKey(string s);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (strlen(arv[1])==26 && validKey(arv[1]))
        {

        }
        else
        {
            printf("Error\n");
            return 1;
        }
    }
    else
    {
        printf ("Error. You must introduce one key and just one.");
        return 1;
    }
}


bool validKey(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {

    }
}