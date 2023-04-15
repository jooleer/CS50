#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // loop through array for amount of candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // check if name in string is found in array
        if (!(strcmp(candidates[i].name, name)))
        {
            // candidate found, add a vote to their name and return true
            candidates[i].votes++;
            return true;
        }
    }
    // no candidate with this name found in array, return false
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    candidate swap;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            // sort candidates from low to high
            if (candidates[j].votes > candidates[i].votes)
            {
                swap = candidates[i];
                candidates[i] = candidates[j];
                candidates[j] = swap;
            }
        }
    }

    for (int i = 0; i < candidate_count; i++)
    {
        printf("%s\n", candidates[i].name);
        if ((i + 1 >= candidate_count) || (candidates[i].votes != candidates[i + 1].votes))
        {
            break;
        }
    }

    return;
}