#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool validKey(string s);
string cifrar(string old, string key);

int main(int argc, string argv[])
{
    string s;
    if (argc == 2)
    {
        if (strlen(argv[1]) == 26 && validKey(argv[1]))
        {
            s = get_string("plaintext:");
            string word = cifrar(s, argv[1]);
            printf("ciphertext: %s\n", word);
        }
        else
        {
            printf("Error. You must introduce a valid key.\n");
            return 1;
        }
    }
    else
    {
        printf("Error. You must introduce one key and just one.\n");
        return 1;
    }
}


bool validKey(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {

        char c = tolower(s[i]);
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
    string new = malloc(strlen(old) * sizeof(char));
    strcpy(new, old);

    //printf ("Dentro de la funcion, la copia es: %s\n", new);
    for (int i = 0; i < strlen(old); i++)
    {
        if (isalpha(old[i]))
        {
            int pos_let = tolower(old[i]) - 'a'; //Posicion de la letra. Por ejemplo, a = 0;
            //printf("post_let = %i\n", pos_let);
            //Distancia entre la letra original y su codificacion. Por ejemplo, a -> c, correccion = 2
            int correccion = tolower(key[pos_let]) - tolower(old[i]);
            //printf("correccion = %i\n", correccion);
            new[i] += correccion;
        }
    }
    return new;
}