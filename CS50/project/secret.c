#include <stdio.h>
#include <stdlib.h>
#include <openssl/aes.h>
#include <openssl/rand.h>

// Prototipos de funciones para cifrar y descifrar
void cifrarAES(unsigned char *textoPlano, int longitudTextoPlano, unsigned char *clave, unsigned char *iv, unsigned char *textoCifrado);
void descifrarAES(unsigned char *textoCifrado, int longitudTextoCifrado, unsigned char *clave, unsigned char *iv, unsigned char *textoPlano);

int main(int argc, char *argv[]) {
    // Verifica los argumentos de la línea de comandos
    if (argc < 5) {
        fprintf(stderr, "Uso: %s <cifrar/descifrar> <archivo de entrada> <archivo de salida> <clave>\n", argv[0]);
        exit(1);
    }

    // Asume que argv[1] es "cifrar" o "descifrar", argv[2] es el archivo de entrada, argv[3] es el archivo de salida, y argv[4] es la clave
    // Aquí iría la lógica para leer el archivo de entrada, cifrarlo o descifrarlo, y escribir el archivo de salida

    return 0;
}




void cifrarAES(unsigned char *textoPlano, int longitudTextoPlano, unsigned char *clave, unsigned char *iv, unsigned char *textoCifrado) {
    AES_KEY aesKey;
    AES_set_encrypt_key(clave, 128, &aesKey); // Prepara la clave para cifrar
    AES_cbc_encrypt(textoPlano, textoCifrado, longitudTextoPlano, &aesKey, iv, AES_ENCRYPT);
}

void descifrarAES(unsigned char *textoCifrado, int longitudTextoCifrado, unsigned char *clave, unsigned char *iv, unsigned char *textoPlano) {
    AES_KEY aesKey;
    AES_set_decrypt_key(clave, 128, &aesKey); // Prepara la clave para descifrar
    AES_cbc_encrypt(textoCifrado, textoPlano, longitudTextoCifrado, &aesKey, iv, AES_DECRYPT);
}
