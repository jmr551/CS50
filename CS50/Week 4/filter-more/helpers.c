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
        for (int j = 0; j < width / 2; j++)
        {
            b = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][width - j].rgbtBlue;
            image[i][width - j].rgbtBlue = b;
            g = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][width - j].rgbtGreen;
            image[i][width - j].rgbtGreen = g;
            r = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][width - j].rgbtRed;
            image[i][width - j].rgbtRed = r;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float r = 0, g = 0, b = 0, count = 0;
            int x0 = i - 1;
            int xf = i + 1;
            int y0 = j - 1;
            int yf = j + 1;

            if (x0 < 0)
            {
                x0 = 0;
            }
            if (y0 < 0)
            {
                y0 = 0;
            }
            if (xf > height - 1)
            {
                xf = height - 1;
            }
            if (yf > width - 1)
            {
                yf = width - 1;
            }
            for (int f = x0; f <= xf; f++)
            {
                for (int c = y0; c <= yf; c++)
                {
                    count += 1;
                    b += (float)image[f][c].rgbtBlue;
                    g += (float)image[f][c].rgbtGreen;
                    r += (float)image[f][c].rgbtRed;
                }
            }
            b /= count;
            g /= count;
            r /= count;

            image[i][j].rgbtBlue = (BYTE)(round(b));
            image[i][j].rgbtGreen = (BYTE)(round(g));
            image[i][j].rgbtRed = (BYTE)(round(r));
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float r = 0, g = 0, b = 0, by = 0;
            int x0 = i - 1;
            int xf = i + 1;
            int y0 = j - 1;
            int yf = j + 1;
            int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
            int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};


            // Para Gx
            for (int f = x0; f <= xf; f++)
            {
                for (int c = y0; c <= yf; c++)
                {
                    if (f >= 0 && f <= height - 1 && c >= 0 && c <= width - 1)
                    {
                        b += (float)image[f][c].rgbtBlue * gx[f - i + 1][c - j + 1] / 9;
                        g += (float)image[f][c].rgbtGreen * gx[f- i + 1][c - j + 1] / 9;
                        r += (float)image[f][c].rgbtRed * gx[f - i + 1][c - j + 1] / 9;

                        b += (float)image[f][c].rgbtBlue * gy[f - i + 1][c - j + 1] / 9;
                        g += (float)image[f][c].rgbtGreen * gy[f- i + 1][c - j + 1] / 9;
                        r += (float)image[f][c].rgbtRed * gy[f - i + 1][c - j + 1] / 9;

                    }
                }
            }

            image[i][j].rgbtBlue = (BYTE)(round(b/2));
            image[i][j].rgbtGreen = (BYTE)(round(g/2));
            image[i][j].rgbtRed = (BYTE)(round(r/2));
        }
    }
    return;
}
