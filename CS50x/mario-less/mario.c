#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do //get pyramid size input from user
    {
        height = get_int("Desired height of pyramid? ");
    }
    while (height < 1 || height > 8);


    int size = 0;
    while (size < height)
    {
        size++;

        //generate spaces
        int width = height;
        while (width > size)
        {
            printf(" ");
            width--;
        }

        //generate blocks
        int pyramid = 0;
        while (pyramid < size)
        {
            printf("#");
            pyramid++;
        }

        printf("\n");

    }
}