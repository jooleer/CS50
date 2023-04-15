// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t bytes[HEADER_SIZE];
    fread(bytes, sizeof(uint8_t) * HEADER_SIZE, 1, input);

    fwrite(bytes, sizeof(uint8_t) * HEADER_SIZE, 1, output);

    // printf("Header file copied successfully.\n");
    int data_size = bytes[40] + (bytes[41] << 8) + (bytes[42] << 16) + (bytes[43] << 24);
    // printf("Data size: %i\n", data_size);

    // TODO: Read samples from input file and write updated data to output file
    int16_t *buffer = malloc((sizeof(int16_t) * data_size));
    int size_read = 0;
    size_read = fread(buffer, sizeof(int16_t), data_size, input);

    for (int i = 0; i < data_size; i++)
    {
        buffer[i] = buffer[i] * factor;
    }

    fwrite(buffer, sizeof(int16_t), size_read, output);

    // Close files
    free(buffer);
    fclose(input);
    fclose(output);
}
