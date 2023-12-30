// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <math.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26*26*26*26; // Elijo hacerlo 4 veces (incluyo el espacio)

// Hash table
node *table[N];

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
    unsigned int num = 0;

    for (int i = 0; i < len; i++)
    {
        num += (tolower(word[len - 1 - i]) - '0') * pot(26, len - i);
    }
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    return false;
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

