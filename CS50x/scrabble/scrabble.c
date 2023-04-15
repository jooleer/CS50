#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int ascii_shift = 97;

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    //Check winner and print output
    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}

int compute_score(string word)
{
    //check each character in word
    int score = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        //process each character and determine if its a valid letter, ignore others
        //increase score depending on POINTS[] value
        if (tolower(word[i]) >= 97 && tolower(word[i]) <= 122)
        {
            int ascii_letter = tolower(word[i]) - ascii_shift;
            score += POINTS[ascii_letter];
        }
    }
    return score;
}