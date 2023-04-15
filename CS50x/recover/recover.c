#include <stdio.h>
#include <stdlib.h>

int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{

    // check arg
    if (argc != 2)
    {
        printf("Incorrect file or input.\n");
        return 1;
    }

    // open input file
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Error opening file %s\n", argv[1]);
        return 2;
    }

    int jpgCount = 0;
    unsigned char buffer[512];
    char filename[16];
    FILE *output = NULL;

    // start reading input file
    while (fread(buffer, BLOCK_SIZE, 1, input) != 0)
    {

        // check if block starts with jpg header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            // if current jpg already exists, close file
            if (jpgCount != 0)
            {
                fclose(output);
            }

            // create filename and open output
            sprintf(filename, "%03i.jpg", jpgCount);
            output = fopen(filename, "w");
            jpgCount++;
        }

        if (output != NULL)
        {
            // write blocks to output file
            fwrite(&buffer, BLOCK_SIZE, 1, output);
        }
    }

    fclose(input);
    fclose(output);
}
