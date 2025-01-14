// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 20000; // Maximo valor de mi funcion hash + 1

// Hash table
static node *table[N]; // estuvo bien convertir a static?

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Asignamos el nodo correspondiente
    unsigned int hashed_num = hash(word);
    node *nodo = table[hashed_num];

    // Comenzamos la búsqueda
    while (nodo != NULL)
    {
        if (strcasecmp(nodo->word, word) == 0)
        {
            return true;
        }
        nodo = nodo->next;
    }

    return false;
}

unsigned int pot(unsigned int a, unsigned int b)
{
    unsigned int res = 1;
    for (int i = 0; i < b; i++)
    {
        res *= a;
    }
    return res;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int len = strlen(word);
    int max_it = len < 3 ? len : 3;
    unsigned int num = 0;

    for (int i = 0; i < max_it; i++)
    {
        num += (tolower(word[len - 1 - i]) - 'a' + 1) * pot(26, i);
    }
    return num % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file_dict = fopen(dictionary, "r");
    if (file_dict == NULL)
    {
        return false;
    }
    int index = 0;
    char new_word[LENGTH + 1];

    // Cada puntero apunta a NULL
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    char c;
    while (fread(&c, sizeof(char), 1, file_dict))
    {
        if (isalpha(c) || c == '\'')
        {
            new_word[index] = tolower(c);
            index++;
        }
        else if (c == '\n')
        {
            new_word[index] = '\0';
            unsigned int hash_num = hash(new_word);
            if (table[hash_num] == NULL)
            {
                node *new_node = malloc(sizeof(node));
                if (new_node == NULL)
                    return false;
                table[hash_num] = new_node;
                table[hash_num]->next = NULL;
                strcpy(table[hash_num]->word, new_word);
                index = 0;
            }
            else
            {
                node *new_node = malloc(sizeof(node));
                if (new_node == NULL)
                    return false;
                strcpy(new_node->word, new_word);
                new_node->next = table[hash_num];
                table[hash_num] = new_node;
                index = 0;
            }
        }
    }
    fclose(file_dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    int c = 0;
    node *cursor = NULL;
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            cursor = table[i];
            c++;

            while (cursor->next != NULL)
            {
                cursor = cursor->next;
                c++;
            }
        }
    }
    return c;
}

// Hago mi función auxiliar

void recursive_unload(node *nodo)
{
    if (nodo->next != NULL)
    {
        recursive_unload(nodo->next);
    }

    free(nodo);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    int c = 0;
    node *cursor = NULL;
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            recursive_unload(table[i]);
        }
    }
    return true;
}
