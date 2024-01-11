#include "helpers.h"
#include <stdio.h> // BORRAR DESPUÉS
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
            printf("SE LE LLAMA A ESTA FUNCION?\n");

        for (int j = 0; j < width; j++)
        {
            //BYTE prom = BYTE(round((float(image[i][j]->rgbtBlue) + float(image[i][j]->rgbtGreen) + float(image[i][j]->rgbtRed))/3));
            // BYTE prom = WORD(DWORD(image[i][j].rgbtBlue) + DWORD(image[i][j].rgbtGreen) + DWORD(image[i][j].rgbtRed))/3;
            if (i == 0 && j == 0)
            {
                printf("numero: %d", int(image[i][j].rgbtBlue));
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
