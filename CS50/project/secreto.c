#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cypherDescypher(FILE *input, FILE *output, int key, int cyp)
{
    srand(key);
    while ((c = fgetc(input)) =! EOF)
    {
        int delta = rand() % (128 - 32); //Generates a pseudorandom number accordind to the seed
        int res;

        if (cyp)
        {
            res = ((c - 32))
        }
    }
}
