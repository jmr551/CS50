#include <cs50.h>
#include <stdio.h>

int count_letters(string s);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    print(count_letters);
}

int count_letters(string s)
{
    int i=0;
    while(s[i]!=0)
    {
        if ((s[i]))
        i++;
    }

}
