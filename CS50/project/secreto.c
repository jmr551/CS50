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
            res = ((c - 32 + delta) % (128 - 32)) + 32;
        }
        else
        {
            res = ((c - 32 - delta + (128 - 32)) % (128 - 32)) + 32;
        }
        fputc(res, output);
    }
}


int main (int argc, char *argv[])
{
    if (argc != 5)
    {
        printf("Usage: %s <enc/des> <key> <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    int cyp = strcmp(argv[1], "enc") == 0;

    if (!cyp && strcmp(argv[1], "des"))
    {
        printf("You should put enc or des to ")
    }
}
