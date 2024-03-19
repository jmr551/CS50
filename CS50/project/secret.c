#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    char *filename = "plain_text.txt"; // Nombre del archivo a leer
    char *buffer;
    long fileLength;

    // Abre el archivo en modo de lectura binaria
    file = fopen(filename, "rb");
    if (file == NULL) {
        perror("Error al abrir el archivo");
        return 1;
    }

    // Busca el final del archivo para determinar su tamaño
    fseek(file, 0, SEEK_END);
    fileLength = ftell(file); // Obtiene el tamaño del archivo
    rewind(file); // Vuelve al inicio del archivo

    // Asigna memoria para almacenar el contenido completo del archivo
    buffer = (char *)malloc((fileLength+1) * sizeof(char));
    if (buffer == NULL) {
        fprintf(stderr, "Error de memoria\n");
        fclose(file);
        return 1;
    }

    // Lee el archivo en el buffer
    fread(buffer, fileLength, 1, file);
    buffer[fileLength] = '\0'; // Asegura que el buffer sea una cadena válida

    // Cierra el archivo
    fclose(file);

    // Aquí puedes procesar el contenido del buffer como desees
    printf("Contenido del archivo:\n%s", buffer);

    // Libera la memoria asignada
    free(buffer);

    return 0;
}
