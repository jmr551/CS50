#include "helpers.h"
#include <stdio.h> // BORRAR DESPUÉS
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //BYTE prom = BYTE(round((float(image[i][j]->rgbtBlue) + float(image[i][j]->rgbtGreen) + float(image[i][j]->rgbtRed))/3));
            // BYTE prom = WORD(DWORD(image[i][j].rgbtBlue) + DWORD(image[i][j].rgbtGreen) + DWORD(image[i][j].rgbtRed))/3;
            if (i == 0 && j == 0)
            {
                uint16_t suma = (uint16_t)image[i][j].rgbtBlue +
                (uint16_t)image[i][j].rgbtGreen +
                (uint16_t)image[i][j].rgbtRed;
                printf("numero: %u\n", image[i][j].rgbtBlue);
                printf("numero: %u\n", image[i][j].rgbtGreen);
                printf("numero: %u\n", image[i][j].rgbtRed);
                printf("numero: %hu\n", float(suma));
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
