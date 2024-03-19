#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>

// Modo de operación
#define MODE CBC

// Tamaño del bloque
#define BLOCK_SIZE AES_BLOCK_SIZE

// Función para leer un archivo en un buffer
char* readFile(char* filename) {
  FILE* file = fopen(filename, "rb");
  if (file == NULL) {
    fprintf(stderr, "Error al abrir el archivo: %s\n", filename);
    return NULL;
  }

  fseek(file, 0, SEEK_END);
  long file_size = ftell(file);
  fseek(file, 0, SEEK_SET);

  char* buffer = malloc(file_size + 1);
  if (buffer == NULL) {
    fprintf(stderr, "Error al asignar memoria\n");
    fclose(file);
    return NULL;
  }

  size_t bytes_read = fread(buffer, 1, file_size, file);
  if (bytes_read != file_size) {
    fprintf(stderr, "Error al leer el archivo: %s\n", filename);
    fclose(file);
    free(buffer);
    return NULL;
  }

  buffer[file_size] = '\0';
  fclose(file);

  return buffer;
}

// Función para escribir un buffer en un archivo
void writeFile(char* filename, char* buffer, long file_size) {
  FILE* file = fopen(filename, "wb");
  if (file == NULL) {
    fprintf(stderr, "Error al abrir el archivo: %s\n", filename);
    return;
  }

  size_t bytes_written = fwrite(buffer, 1, file_size, file);
  if (bytes_written != file_size) {
    fprintf(stderr, "Error al escribir el archivo: %s\n", filename);
  }

  fclose(file);
}

// Función para encriptar un archivo
int encryptFile(char* input_file, char* output_file, char* key, int key_size) {
  // Generar vector de inicialización (IV) aleatorio
  unsigned char iv[BLOCK_SIZE];
  RAND_bytes(iv, BLOCK_SIZE);

  // Crear contexto de encriptación
  AES_KEY enc_key;
  if (AES_set_encrypt_key((const unsigned char*)key, key_size * 8, &enc_key) < 0) {
    fprintf(stderr, "Error al configurar la clave de encriptación\n");
    return 1;
  }

  // Abrir archivos
  FILE* input = fopen(input_file, "rb");
  if (input == NULL) {
    fprintf(stderr, "Error al abrir el archivo de entrada: %s\n", input_file);
    return 1;
  }

  FILE* output = fopen(output_file, "wb");
  if (output == NULL) {
    fprintf(stderr, "Error al abrir el archivo de salida: %s\n", output_file);
    fclose(input);
    return 1;
  }

  // Escribir IV al archivo de salida
  fwrite(iv, 1, BLOCK_SIZE, output);

  // Buffer para almacenar datos
  unsigned char buffer[BLOCK_SIZE];
  int bytes_read;

  // Encriptar y escribir datos en el archivo de salida
  while ((bytes_read = fread(buffer, 1, BLOCK_SIZE, input)) > 0) {
    AES_cbc_encrypt(buffer, buffer, bytes_read, &enc_key, iv, MODE);
    fwrite(buffer, 1, bytes_read, output);
  }

  // Cerrar archivos
  fclose(input);
  fclose(output);

  return 0;
}
// Función para desencriptar un archivo
int decryptFile(char* input_file, char* output_file, char* key, int key_size) {
  // Leer IV del archivo de entrada
  unsigned char iv[BLOCK_SIZE];
  FILE* input = fopen(input_file, "rb");
  if (input == NULL) {
    fprintf(stderr, "Error al abrir el archivo de entrada: %s\n", input_file);
    return 1;
  }

  fread(iv, 1, BLOCK_SIZE, input);

  // Crear contexto de desencriptación
  AES_KEY dec_key;
  if (AES_set_decrypt_key((const unsigned char*)key, key_size * 8, &dec_key) < 0) {
    fprintf(stderr, "Error al configurar la clave de desencriptación\n");
    fclose(input);
    return 1;
  }

  // Abrir archivos
  FILE* output = fopen(output_file, "wb");
  if (output == NULL) {
    fprintf(stderr, "Error al abrir el archivo de salida: %s\n", output_file);
    fclose(input);
    return 1;
  }

  // Buffer para almacenar datos
  unsigned char buffer[BLOCK_SIZE];
  int bytes_read;

  // Desencriptar y escribir datos en el archivo de salida
  while ((bytes_read = fread(buffer, 1, BLOCK_SIZE, input)) > 0) {
    AES_cbc_decrypt(buffer, buffer, bytes_read, &dec_key, iv, MODE);
    fwrite(buffer, 1, bytes_read, output);
  }

  // Cerrar archivos
  fclose(input);
  fclose(output);

  return 0;
}

// Función para mostrar ayuda
void printHelp() {
  printf("Uso: %s [opción] archivo_entrada archivo_salida clave\n", "aes_encrypt_decrypt");
  printf("Opciones:\n");
  printf("  -e  Encriptar archivo\n");
  printf("  -d  Desencriptar archivo\n");
  printf("  -h  Mostrar ayuda\n");
}

// Función principal
int main(int argc, char* argv[]) {
  if (argc < 5) {
    printHelp();
    return 1;
  }

  char* option = argv[1];
  char* input_file = argv[2];
  char* output_file = argv[3];
  char* key = argv[4];

  int key_size = strlen(key);
  if (key_size < 16) {
    fprintf(stderr, "La clave debe tener al menos 16 caracteres\n");
    return 1;
  }

  if (strcmp(option, "-e") == 0) {
    return encryptFile(input_file, output_file, key, key_size);
  } else if (strcmp(option, "-d") == 0) {
    return decryptFile(input_file, output_file, key, key_size);
  } else {
    printHelp();
    return 1;
  }

  return 0;
}
