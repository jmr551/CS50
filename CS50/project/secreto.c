#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cypherDescypher(FILE *input, FILE *output, int key, int cyp)
{
    srand(key); // Initialise the random number generator with the seed (key)
    int c;
    while ((c = fgetc(input)) != EOF)
    {
        if (c == '\n' || c == '\r') {
            fputc(c, output); // Preserve newlines and carriage returns
        }
        else
        {
            int delta = rand() % (127 - 32); //Generates a pseudorandom number according to the seed
            int res;

            if (cyp)
            {
                res = ((c - 32 + delta) % (127 - 32)) + 32; // Encrypt the character
            }
            else
            {
                res = ((c - 32 - delta + (127 - 32)) % (127 - 32)) + 32; // Decrypt the character
            }
            fputc(res, output); // Write the result to the output file
        }
    }
}


int main (int argc, char *argv[])
{
    if (argc != 5)
    {
        printf("Usage: %s <enc/dec> <key> <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    int cyp = strcmp(argv[1], "enc") == 0;

    if (!cyp && strcmp(argv[1], "dec"))
    {
        printf("You should put enc or dec to encrypt or decrypt\n");
        return 2;
    }

    int key = atoi(argv[2]);
    FILE *input = fopen(argv[3], "r");
    if (!input)
    {
        printf("Error. Could not open the input file.\n");
        return 3;
    }

    FILE *output = fopen(argv[4], "w");
    if (!output)
    {
        printf("Error. Could not open the output file.\n");
        return 4;
    }

    cypherDescypher(input, output, key, cyp);

    fclose(input);
    fclose(output);

    return 0;
}
