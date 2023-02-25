// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
string replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels.c word\n");
        return 1;
    }
    string converted = replace(argv[1]);

    printf("%s\n", converted);

    return 0;
}

string replace(string word)
{
    string hola;
    strcpy (hola, word);
    for (int i = 0; i < strlen(hola); i++)
    {
        switch (hola[i])
        {
            case 'a':
                hola[i] = (char) '6';
                break;
            case 'e':
                hola[i] = (char) '3';
                break;
            case 'i':
                hola[i] = (char) '1';
                break;
            case 'o':
                hola[i] = (char) '0';
                break;
            default:
                hola[i] = word [i];
                break;
        }
    }
    return hola;
}
