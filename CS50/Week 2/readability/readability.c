#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int count_letters(string s);
int count_words(string s);
int count_sentences(string s);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    printf("%i letters\n", letters);
    printf("%i words\n", words);
    printf("%i sentences\n", sentences);
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