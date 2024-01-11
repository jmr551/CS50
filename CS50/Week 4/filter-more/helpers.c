#include "helpers.h"
#include <math.h>
#include <stdio.h> // BORRAR DESPUÉS
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE prom = (BYTE) round(((float)image[i][j].rgbtBlue + (float)image[i][j].rgbtGreen + (float)image[i][j].rgbtRed)/3);
            image[i][j].rgbtBlue = prom;
            image[i][j].rgbtGreen = prom;
            image[i][j].rgbtRed = prom;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    BYTE r, g, b;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            
            image[i][j].rgbtBlue = prom;
            image[i][j].rgbtGreen = prom;
            image[i][j].rgbtRed = prom;
        }
    }
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
