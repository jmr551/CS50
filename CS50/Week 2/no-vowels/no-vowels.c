// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
void replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels.c word\n");
        return 1;
    }
    replace(argv[1]);

    printf("%s\n", argv[1]);

    return 0;
}

void replace(string word)
{
    for (int i = 0; i < strlen(word); i++)
    {
        switch (word[i])
        {
            case 'a':
                word[i] = (char) '6';
                break;
            case 'e':
                word[i] = (char) '3';
                break;
            case 'i':
                word[i] = (char) '1';
                break;
            case 'o':
                word[i] = (char) '0';
                break;
            default:
                word[i] = word [i];
                break;
        }
    }
}
