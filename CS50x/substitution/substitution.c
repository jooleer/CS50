#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void cypher(string key, string text);

int main(int argc, string argv[])
{
    // check if correct amount of args are given
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // check if key is 26 characters long
    int length = strlen(argv[1]);
    if (length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // check if all 26 characters are alphabetical
    string string_check = argv[1];
    int check_alpha = 0;
    while (check_alpha < length)
    {
        if (!isalpha(string_check[check_alpha]))
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        check_alpha++;
    }

    // duplicate letters check
    int duplicate_letters = 0;
    int duplicate_letters_nested = 0;
    while (duplicate_letters < length)
    {
        while (duplicate_letters_nested < length)
        {
            if (duplicate_letters != duplicate_letters_nested)
            {
                if ((int)tolower(string_check[duplicate_letters]) == (int)tolower(string_check[duplicate_letters_nested]))
                {
                    // duplicate character detected
                    printf("Key must contain 26 characters.");
                    return 1;
                }
            }
            duplicate_letters_nested++;
        }
        duplicate_letters++;
        duplicate_letters_nested = 0;
    }

    // variables for cipher function
    string cypher_key = argv[1];
    string cypher_text = get_string("plaintext: ");

    // calculate text
    cypher(cypher_key, cypher_text);
}

void cypher(string key, string text)
{
    string output = text;

    // check for each character its alphabetical position and swap it with given key
    int position = 0;
    while ((char)text[position] != 0)
    {
        if (isalpha(text[position]))
        {
            if (islower(text[position]))
            {
                int character = text[position] - 97;
                int swap = tolower(key[character]);
                output[position] = swap;
            }
            else
            {
                int character = text[position] - 65;
                int swap = toupper(key[character]);
                output[position] = swap;
            }
        }
        position++;
    }

    // output result to user
    printf("ciphertext: %s\n", output);
}