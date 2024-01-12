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
    char file_name[8];
    bool abierto = false;
    while (fread(buffer, 1, 512, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0)==0xe0)
        {
            sprintf(file_name, "%03d.jpg",cont);
            FILE *nueva_foto = fopen(file_name, "w");
            abierto = true;
            fwrite(buffer, 1, 512, nueva_foto);
            cont++;
        }
        else if(abierto)
        {
            fwrite(buffer, 1, 512, nueva_foto);
        }
    }

    fclose (file);
}
