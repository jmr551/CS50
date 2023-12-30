// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 18279; // Maximo valor de mi funcion hash + 1

// Hash table
static node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
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
    unsigned int len = strlen(word);
    printf("len = %d\n", len);
    int max_it = len < 3 ? len : 3;
    printf ("max_it = %d\n", max_it);
    unsigned int num = 0;

    for (int i = 0; i < max_it; i++)
    {
        num += (tolower(word[len - 1 - i]) - 'a' + 1) * pot(26, i);
    }
    return num;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file_dict = fopen(dictionary, "r");
    if (file_dict == NULL)
    {
        return false;
    }

    
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}

