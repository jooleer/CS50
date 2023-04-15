// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 64;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);
    node *scan = table[index];
    while (scan != NULL)
    {
        if (strcasecmp(scan->word, word) == 0)
        {
            //if word is in dictionary return true
            return true;
        }
        else
        {
            //if word not found, go to next location in linked list
            scan = scan->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //cache word and make lowercase for hashing
    char cache_word[strlen(word) + 1];
    for (int i = 0; i < strlen(word); i++)
    {
        cache_word[i] = tolower(word[i]);
    }

    cache_word[strlen(word)] = '\0';

    unsigned int hash = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash = (hash << 2) ^ cache_word[i];
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];

    while (fscanf(file, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        strcpy(n->word, buffer);

        unsigned int index = hash(buffer);

        if (table[index] != NULL)
        {
            n->next = table[index];
        }
        else
        {
            n->next = NULL;
        }

        table[index] = n;
        word_count++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{

    return word_count;
}

//recursive memory freeing function
void clear_memory(node *t)
{
    if (t->next != NULL)
    {
        clear_memory(t->next);
    }
    free(t);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    int u = 0;
    while (u < N)
    {
        if (table[u] != NULL)
        {
            clear_memory(table[u]);
        }
        u++;
    }
    return true;
}