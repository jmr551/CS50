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

    while (fgets(buffer, sizeof(buffer), archivo) != NULL) {
        printf("%s", buffer); // Imprime cada línea leída
    }

    // Cierra el archivo
    fclose(archivo);

    return 0; // Finaliza con éxito
}
