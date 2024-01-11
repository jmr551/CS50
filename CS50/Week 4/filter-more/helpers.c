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
            // BYTE prom = (float(image[i][j]->rgbtBlue) + float(image[i][j]->rgbtGreen) + float(image[i][j]->rgbtRed))/3;
            printf("%f",float(image[i][j].rgbtBlue)/3);
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
