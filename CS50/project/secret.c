#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE *archivo;
    char buffer[1024];

    if (argc < 2) {
        printf("Usage: %s <file>\n", argv[0]);
        return 1;
    }

    archivo = fopen(argv[1], "r");
    if (archivo == NULL) {
        perror("Error");
        return 2; // Retorna 1 para indicar un error
    }

    // Lee el contenido del archivo en el búfer
    // Esta simple demostración asume que el contenido del archivo es menor que el tamaño del búfer
    if (fgets(buffer, sizeof(buffer), archivo) != NULL) {
        printf("Contenido del archivo: %s", buffer);
    } else {
        printf("No se pudo leer el contenido del archivo o el archivo está vacío.\n");
    }

    // Cierra el archivo
    fclose(archivo);

    return 0; // Finaliza con éxito
}
