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
    char file_name[];
    while (fread(buffer, 1, 512, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0)==0xe0)
        {
            printf("Encontramos la foto %d\n", cont+1);
            // Grabamos la foto...
            sprintf(file_name, "%d",cont);
            printf("%s\n", file_name);
            cont++;
        }
    }

    fclose (file);
}
