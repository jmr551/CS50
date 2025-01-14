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
            BYTE prom =
                (BYTE) round(((float) image[i][j].rgbtBlue + (float) image[i][j].rgbtGreen + (float) image[i][j].rgbtRed) / 3);
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
            image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;
            image[i][width - 1 - j].rgbtBlue = b;
            g = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            image[i][width - 1 - j].rgbtGreen = g;
            r = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
            image[i][width - 1 - j].rgbtRed = r;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float r = 0, g = 0, b = 0, count = 0;
            int x0 = i - 1;
            int xf = i + 1;
            int y0 = j - 1;
            int yf = j + 1;
            /*
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
            */
            for (int f = x0; f <= xf; f++)
            {
                for (int c = y0; c <= yf; c++)
                {
                    if (f >= 0 && f <= height - 1 && c >= 0 && c <= width - 1)
                    {
                        count += 1;
                        b += (float) image[f][c].rgbtBlue;
                        g += (float) image[f][c].rgbtGreen;
                        r += (float) image[f][c].rgbtRed;
                    }
                }
            }
            b /= count;
            g /= count;
            r /= count;

            new_image[i][j].rgbtBlue = (BYTE) (round(b));
            new_image[i][j].rgbtGreen = (BYTE) (round(g));
            new_image[i][j].rgbtRed = (BYTE) (round(r));
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float rx = 0, ry = 0, gx = 0, gy = 0, bx = 0, by = 0;
            int x0 = i - 1;
            int xf = i + 1;
            int y0 = j - 1;
            int yf = j + 1;
            int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
            int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

            for (int f = x0; f <= xf; f++)
            {
                for (int c = y0; c <= yf; c++)
                {
                    if (f >= 0 && f <= height - 1 && c >= 0 && c <= width - 1)
                    {
                        // printf("%d - %d\n", f - i + 1, c - j + 1);
                        bx += (float) image[f][c].rgbtBlue * Gx[f - i + 1][c - j + 1];
                        gx += (float) image[f][c].rgbtGreen * Gx[f - i + 1][c - j + 1];
                        rx += (float) image[f][c].rgbtRed * Gx[f - i + 1][c - j + 1];

                        by += (float) image[f][c].rgbtBlue * Gy[f - i + 1][c - j + 1];
                        gy += (float) image[f][c].rgbtGreen * Gy[f - i + 1][c - j + 1];
                        ry += (float) image[f][c].rgbtRed * Gy[f - i + 1][c - j + 1];
                    }
                }
            }
            float b = sqrt(bx * bx + by * by);
            float g = sqrt(gx * gx + gy * gy);
            float r = sqrt(rx * rx + ry * ry);
            if (b < 0)
                b = 0;
            if (g < 0)
                g = 0;
            if (r < 0)
                r = 0;
            if (b > 255)
                b = 255;
            if (g > 255)
                g = 255;
            if (r > 255)
                r = 255;

            new_image[i][j].rgbtBlue = (BYTE) (round(b));
            new_image[i][j].rgbtGreen = (BYTE) (round(g));
            new_image[i][j].rgbtRed = (BYTE) (round(r));
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = new_image[i][j].rgbtBlue;
            image[i][j].rgbtGreen = new_image[i][j].rgbtGreen;
            image[i][j].rgbtRed = new_image[i][j].rgbtRed;
        }
    }
    return;
}
