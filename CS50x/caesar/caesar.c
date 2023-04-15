#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int only_digits(string argv);
int calculate_key(int argv);
int power_of(int x, int y);
void cipher(string cipher_input, int shift);

int main(int argc, string argv[])
{
    // check if correct number of arguments are entered, exit if not
    if (argc > 2 || argc < 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = only_digits(argv[1]);

    // if return from key is -1 non-digit is detected and we exit
    if (key == -1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int shift = calculate_key(key);
    string cipher_input = get_string("plaintext: ");
    cipher(cipher_input, shift);
}

// check if only digits are used and calculate key
int only_digits(string argv)
{
    int key = 0;
    int len = strlen(argv);

    for (int check_digit = 0, length = strlen(argv); check_digit < length; check_digit++)
    {
        // if non-digits are detected return -1 to exit
        if (!isdigit(argv[check_digit]))
        {
            return -1;
        }

        key += (argv[check_digit] - 48) * power_of(10, (length - check_digit - 1));
    }
    return key;
}

// if key (alphabet shift) is larger than 26 reduce it until its lower than 26
int calculate_key(int key)
{
    if (key > 26)
    {
        while (key > 26)
        {
            key -= 26;
        }
    }

    return key;
}

// power calculation
int power_of(int x, int y)
{
    int result = 0;
    if (y == 0)
    {
        return 1;
    }

    if (x == 0)
    {
        return 0;
    }

    return x * power_of(x, y - 1);
}

// convert user cipher input to encrypted output
void cipher(string cipher_input, int shift)
{
    int length = strlen(cipher_input);
    string cipher_output = cipher_input;
    for (int i = 0; i < length; i++)
    {
        // capital letters processing
        if (cipher_input[i] >= 65 && cipher_input[i] <= 90)
        {
            // if larger than 90 we go back to beginning of alphabet
            if (cipher_input[i] + shift > 90)
            {
                cipher_output[i] = cipher_input[i] + shift - 26;
            }
            else
            {
                cipher_output[i] = cipher_input[i] + shift;
            }
        }
        else if (cipher_input[i] >= 97 && cipher_input[i] <= 122)
        {
            // if larger than 122 we go back to start of alphabet
            if (cipher_input[i] + shift > 122)
            {
                cipher_output[i] = cipher_input[i] + shift - 26;
            }
            else
            {
                cipher_output[i] = cipher_input[i] + shift;
            }
        }
        else
        {
            cipher_output[i] = cipher_input[i];
        }
    }
    // output ciphered text to user
    printf("ciphertext: %s\n", cipher_output);
}