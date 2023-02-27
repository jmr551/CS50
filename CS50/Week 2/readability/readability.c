#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int count_letters(string s);
int count_words(string s);
int count_sentences(string s);

int main(void)
{
    float L, S, index;
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    L = 100.0 * letters / words;
    S = 100.0 * sentences / words;
    index = 0.0588 * L - 0.296 * S - 15.8;

    printf("%i letters\n", letters);
    printf("%i words\n", words);
    printf("%i sentences\n", sentences);
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}

int count_letters(string s)
{
    int i=0, c=0;
    while(s[i]!=0)
    {
        if (isalpha(s[i]))
        {
            c++;
        }
        i++;
    }
    return c;
}


int count_words(string s)
{
    int i=0, c=0;
    while(s[i]!=0)
    {
        if (s[i]== ' ')
        {
            c++;
        }
        i++;
    }
    return c+1;
}

int count_sentences(string s)
{
    int i=0, c=0;
    while(s[i]!=0)
    {
        if (s[i]== '.' || s[i]== '!' || s[i]== '?')
        {
            c++;
        }
        i++;
    }
    return c;
}