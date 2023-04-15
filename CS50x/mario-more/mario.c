#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get input from user
    int size;
    do
    {
        size = get_int("Enter size of desired pyramids: ");
    }
    while (size < 1 || size > 8);

    //start building the pyramids
    int height = 0;
    while (height < size)
    {
        height++;
        //create front spaces
        int front_spaces = size;
        while (front_spaces > height)
        {
            printf(" ");
            front_spaces--;
        }

        //generate front blocks
        int front_blocks = 0;
        while (front_blocks < height)
        {
            printf("#");
            front_blocks++;
        }

        //center separator space
        printf("  ");

        //generate back blocks
        int back_blocks = 0;
        while (back_blocks < height)
        {
            printf("#");
            back_blocks++;
        }

        printf("\n");
    }
}
