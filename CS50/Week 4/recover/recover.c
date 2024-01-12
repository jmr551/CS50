#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Favor especificar el nombre del archivo\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("No se puede abrir el archivo\n");
        return 1;
    }
    uint8_t buffer[512];

    int cont = 0;
    while (fread(buffer, 1, 512, file))
    {
        
    }

    fclose (file);
}
