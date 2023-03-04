#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool validKey(string s);
string cifrar(string old, string key);

int main(int argc, string argv[])
{
    string s, word;
    if (argc == 2)
    {
        if (strlen(argv[1])==26 && validKey(argv[1]))
        {
            s = get_string("plaintext:");
            word = cifrar(s, argv[1]);
        }
        else
        {
             printf("Error. You must introduce a valid key.\n");
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

        c = tolower(s[i]);
        if (isalpha(s[i]))
        {
            for (int j = 0; j < i; j++)
            {
                if (c == tolower(s[j]))
                {
                    return false;
                }
            }
        }
        else
        {
            return false;
        }
    }
    return true;
}

string cifrar(string old, string key)
{
    string new;
    strcpy(new, old);

    for (int i = 0; i < str(len(new)); i++)
    {
        if (isalpha(old[i]))
        {
            int correccion = tolower()
        }
    }
}