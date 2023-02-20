#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int pares = 0, impares = 0;
    long card = get_long("Number: ");
    long card_copia = card;
    bool visa = false, master = false, checksum = false;

    // Verificamos primero el checksum
    int i;
    for (i = 0; i < 16; i++)
    {
        if (i % 2 == 0) impares += card_copia % 10;
        else
        {
            int n = 2* (card_copia % 10);
            pares += n % 10 + n/10;
        }
        card_copia /= 10;
        if (card_copia < 1) break;
    }
    checksum = ((pares + impares) % 10 == 0) && (i<=16) && (i>=13);
    printf("Cant de digitos: %d\n", i);
    //printf("Pares: %i\n", pares);
    //printf("Impares: %i\n", impares);

    if (checksum)
    {
        long two_digits = card;
        while ( two_digits > 100)
        {
            two_digits/=10;
        }
        if (two_digits == 34 || two_digits == 37) printf("AMEX\n");
        else if (two_digits >= 40 && two_digits <= 49) printf("VISA\n");
        else if (two_digits >= 51 && two_digits <= 55) printf("MASTERCARD\n");
        else printf("INVALID\n");
    }
    else printf("INVALID\n");

}