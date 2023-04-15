#include <cs50.h>
#include <stdio.h>

// constants
const string INVALID = "INVALID\n";

// declare functions
long get_number(void);

int main(void)
{
    long card_number = get_number();
}

// function to get card number and calculate validity and card type
long get_number(void)
{

    long card_number;
    // ask user to input card number
    do
    {
        card_number = get_long("Enter your card number: ");
    }

    while (card_number < 0);

    int length = 0;
    long card_number2 = card_number;
    while (card_number2 > 0)
    {
        card_number2 = card_number2 / 10;
        length++;
    }
    if (length > 16 || length < 13)
    {
        printf("%s", INVALID);
        return 0;
    }
    else
    {
        int digits = 0;
        int calculate_digit = 0;
        int last_digit = 0;
        card_number2 = card_number;
        while (card_number2 > 0)
        {
            last_digit += card_number2 % 10;
            card_number2 = card_number2 / 10;
            int temp_digit = (card_number2 % 10) * 2;
            if (temp_digit > 9)
            {
                printf("Temp digit: %i\n", temp_digit);
                int temp_digit2 = temp_digit % 10;
                printf("Temp digit 2: %i\n", temp_digit2);
                temp_digit = (temp_digit / 10) + temp_digit2;
                printf("Temp digit: %i\n", temp_digit);
            }

            calculate_digit += temp_digit;
            card_number2 = card_number2 / 10;
            digits++;

            printf("Last Digit: %i\n", last_digit);
            printf("Calculate Digit: %i\n", calculate_digit);
        }

        printf("Digit calculation: %i\n", calculate_digit);

        calculate_digit += last_digit;

        /*
        Determine card type

        Card Type       Digits      Starting numbers
        AMEX            15          34, 37
        MASTERCARD      16          51, 52, 53, 54, 55
        VISA            13/16       4
        */

        if (calculate_digit % 10 == 0)
        {
            printf("Number validated: %i\n", calculate_digit);
            printf("Card Number: %li\n", card_number);
            while (card_number >= 100)
            {
                card_number = card_number / 10;
            }
            if (card_number / 10 == 4)
            {
                printf("VISA\n");
            }
            else if (card_number / 10 == 3 && (card_number % 10 == 4 || card_number % 10 == 7))
            {
                printf("AMEX\n");
            }
            else if (card_number / 10 == 5 &&
                     (card_number % 10 == 1 || card_number % 10 == 2 || card_number % 10 == 3 || card_number % 10 == 4 || card_number % 10 == 5))
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("%s", INVALID);
            }
        }
        else
        {
            printf("%s", INVALID);
        }
    }

    return card_number;
}