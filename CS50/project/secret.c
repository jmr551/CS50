#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cifrarDescifrar(FILE *entrada, FILE *salida, int clave, int cifrar) {
    srand(clave); // Establece la semilla para la generación de números aleatorios
    int c;
    while ((c = fgetc(entrada)) != EOF) {
        int delta = rand() % (128 - 32); // Genera un número aleatorio dentro del rango ajustado
        int resultado;
        if (cifrar) {
            resultado = ((c - 32 + delta) % (128 - 32)) + 32; // Cifrado
        } else {
            resultado = ((c - 32 - delta + (128 - 32)) % (128 - 32)) + 32; // Descifrado, ajuste para el módulo negativo
        }
        fputc(resultado, salida);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        fprintf(stderr, "Uso: %s <enc/des> <clave> <archivo de entrada> <archivo de salida>\n", argv[0]);
        return 1;
    }

    int cifrar = strcmp(argv[1], "enc") == 0;
    if (!cifrar && strcmp(argv[1], "des") != 0) {
        fprintf(stderr, "El primer argumento debe ser 'enc' para encriptar o 'des' para desencriptar.\n");
        return 1;
    }

    int clave = atoi(argv[2]);
    FILE *entrada = fopen(argv[3], "r");
    if (!entrada) {
        perror("Error al abrir el archivo de entrada");
        return 1;
    }

    FILE *salida = fopen(argv[4], "w");
    if (!salida) {
        perror("Error al abrir el archivo de salida");
        fclose(entrada); // Asegura que el archivo de entrada se cierre antes de salir
        return 1;
    }

    cifrarDescifrar(entrada, salida, clave, cifrar);

    fclose(entrada);
    fclose(salida);

    return 0;
}
