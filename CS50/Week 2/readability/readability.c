#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int count_letters(string s);
int count_words(string s);


int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    printf("%i letters\n", letters);
    printf("%i words\n", words);
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