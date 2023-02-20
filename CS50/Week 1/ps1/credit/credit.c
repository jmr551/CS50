#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int pares = 0, impares = 0;
    long card = get_long("Number: ");
    long card_copia = card;
    bool visa = false, master = false, checksum = false;

    // Verificamos primero el checksum
    for (int i = 0; i < 16; i++)
    {
        if (i % 2 == 0) impares += card_copia % 10;
        else
        {
            int n = 2* (card_copia % 10);
            pares += n % 10 + n/10;
        }
        card_copia/=10;
    }
    checksum = ((pares + impares) % 10 == 0);

    //printf("Pares: %i\n", pares);
    //printf("Impares: %i\n", impares);

    if (checksum)
    {
        int two_digits = card/10000000000000;
        printf("%d\n", two_digits);
        if (two_digits == 34 || two_digits == 37) printf("AMEX\n");
        else if (two_digits == 40) printf("VISA\n");
        else if (two_digits >= 51 && two_digits <= 55) printf("MASTERCARD\n");
        else printf("The what?\n");
    }
    else printf("INVALID\n");

}