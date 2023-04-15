#include "helpers.h"
#include "math.h"
#include "stdio.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;
            float average = (blue + green + red) / 3.0;
            image[i][j].rgbtBlue = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtRed = round(average);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            temp[i][j] = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp[i][j];
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    // copy image data into copy first
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avgBlue = 0;
            int avgGreen = 0;
            int avgRed = 0;
            int averageCount = 0;

            for (int n = -1; n < 2; n++)
            {
                for (int m = -1; m < 2; m++)
                {
                    int x = n + i;
                    int y = m + j;

                    if (!(x < 0) && !(x > height - 1) && !(y < 0) && !(y > width - 1))
                    {
                        avgBlue += copy[x][y].rgbtBlue;
                        avgGreen += copy[x][y].rgbtGreen;
                        avgRed += copy[x][y].rgbtRed;

                        averageCount++;
                    }
                }
            }
            int blurBlue = round((float)avgBlue / averageCount);
            int blurGreen = round((float)avgGreen / averageCount);
            int blurRed = round((float)avgRed / averageCount);

            image[i][j].rgbtBlue = blurBlue;
            image[i][j].rgbtGreen = blurGreen;
            image[i][j].rgbtRed = blurRed;
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height + 2][width + 2];
    // copy image data into copy first
    for (int i = -1; i < height + 1; i++)
    {
        for (int j = -1; j < width + 1; j++)
        {
            if (i == -1 || i == height + 1 || j == -1 || j == width + 1)
            {
                copy[i][j].rgbtBlue = 0;
                copy[i][j].rgbtGreen = 0;
                copy[i][j].rgbtRed = 0;
            }
            else
            {
                copy[i][j] = image[i][j];
            }
        }
    }

    //
    int Gx[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    int Gy[] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int edgeBlueX = 0;
            int edgeGreenX = 0;
            int edgeRedX = 0;
            int edgeBlueY = 0;
            int edgeGreenY = 0;
            int edgeRedY = 0;
            int edgeCount = 0;

            for (int n = -1; n < 2; n++)
            {
                for (int m = -1; m < 2; m++)
                {
                    int x = n + i;
                    int y = m + j;

                    if (!(x < 0) && !(x > height - 1) && !(y < 0) && !(y > width - 1))
                    {
                        int tempBlueX = copy[x][y].rgbtBlue * Gx[edgeCount];
                        int tempGreenX = copy[x][y].rgbtGreen * Gx[edgeCount];
                        int tempRedX = copy[x][y].rgbtRed * Gx[edgeCount];

                        edgeBlueX += tempBlueX;
                        edgeGreenX += tempGreenX;
                        edgeRedX += tempRedX;

                        int tempBlueY = copy[x][y].rgbtBlue * Gy[edgeCount];
                        int tempGreenY = copy[x][y].rgbtGreen * Gy[edgeCount];
                        int tempRedY = copy[x][y].rgbtRed * Gy[edgeCount];

                        edgeBlueY += tempBlueY;
                        edgeGreenY += tempGreenY;
                        edgeRedY += tempRedY;

                        edgeCount++;
                    }
                    else
                    {
                        edgeCount++;
                    }
                }
            }

            int newBlue = round(sqrt((edgeBlueX * edgeBlueX) + (edgeBlueY * edgeBlueY)));
            int newGreen = round(sqrt((edgeGreenX * edgeGreenX) + (edgeGreenY * edgeGreenY)));
            int newRed = round(sqrt((edgeRedX * edgeRedX) + (edgeRedY * edgeRedY)));

            if (newBlue > 255)
            {
                newBlue = 255;
            }
            if (newGreen > 255)
            {
                newGreen = 255;
            }
            if (newRed > 255)
            {
                newRed = 255;
            }

            image[i][j].rgbtBlue = newBlue;
            image[i][j].rgbtGreen = newGreen;
            image[i][j].rgbtRed = newRed;
        }
    }
}
