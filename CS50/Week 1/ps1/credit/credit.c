#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int pares = 0, impares = 0;
    long card = get_long();
    long card_copia = card;
    bool visa = false, master = false, checsum = false;

    // Verificamos primero el checksum
    for (int i = 0; i < 16; i++)
    {
        if (i % 2 == 0) impares += card_copia % 10;
        else pares += 2* card_copia % 10;
        card_copia/=10;
    }
    checksum = ((pares + impares) % 10 == 0);
    printf(checksum);
}