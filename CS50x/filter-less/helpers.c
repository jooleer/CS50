#include "helpers.h"
#include "stdio.h"
#include "math.h"
#include "stdlib.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get original color values from image
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;

            // calculate average color of the pixel to set grayscale
            float combined = (red + green + blue) / 3.0;

            // round number and convert to integer
            int average = round(combined);

            // output the grayscale color to image
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get original color values from image
            int originalBlue = image[i][j].rgbtBlue;
            int originalGreen = image[i][j].rgbtGreen;
            int originalRed = image[i][j].rgbtRed;

            // convert colors to sepia tones
            float sRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            float sGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            float sBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;

            // limit color value to 255
            int sepiaRed = round(sRed);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            int sepiaGreen = round(sGreen);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            int sepiaBlue = round(sBlue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // output sepia colors to image
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // set temporary variable to store data for swapping
    RGBTRIPLE tempimg[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            // store data from first pixel in temp variable
            tempimg[i][j] = image[i][j];

            // set first pixel in width to last pixel -i
            image[i][j] = image[i][width - 1 - j];

            // set last pixel -i in width to first.
            image[i][width - 1 - j] = tempimg[i][j];
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    // loop to copy image into copy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // loop to blur image

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int countBlue = 0;
            int countGreen = 0;
            int countRed = 0;
            int countAverage = 0;
            for (int m = -1; m < 2; m++)
            {
                for (int n = -1; n < 2; n++)
                {
                    int x = i + m;
                    int y = j + n;

                    if (!(x < 0) && !(y < 0) && !(x > height - 1) && !(y > width - 1))
                    {
                        countBlue += copy[x][y].rgbtBlue;
                        countGreen += copy[x][y].rgbtGreen;
                        countRed += copy[x][y].rgbtRed;
                        countAverage++;
                    }
                }
            }

            image[i][j].rgbtBlue = round((float)countBlue / countAverage);
            image[i][j].rgbtGreen = round((float)countGreen / countAverage);
            image[i][j].rgbtRed = round((float)countRed / countAverage);
        }
    }
}