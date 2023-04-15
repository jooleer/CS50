#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

void calculate_level(string text);

int main(void)
{
    // ask user to input text
    string text = get_string("Text: ");

    // call function to determine reading level
    calculate_level(text);
}

void calculate_level(string text)
{
    int letters = 0;
    int sentences = 0;
    int words = 1;
    int location = 0;

    // Count amount of letters, words and sentences
    while (text[location] != 0)
    {
        // if character is a-z count towards letters
        if (tolower(text[location]) >= 97 && tolower(text[location]) <= 122)
        {
            letters++;
            location++;
        }
        // if character is punctuation (!?.) count towards sentences
        else if (text[location] == 33 || text[location] == 63 || text[location] == 46)
        {
            sentences++;
            location++;
        }
        // count spaces between characters to count words
        else if (text[location] == 32)
        {
            words++;
            location++;
        }
        else
        {
            location++;
        }
    }

    // index = 0.0588 * L - 0.296 * S - 15.8
    // L = avg letters per 100 words, S = avg sentences per 100 words

    float L = (letters / (float)words) * 100;
    float S = (sentences / (float)words) * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rating = round(index);

    if (rating < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (rating > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rating);
    }
}