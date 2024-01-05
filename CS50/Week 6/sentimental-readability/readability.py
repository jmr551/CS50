import cs50

text = cs50.get_string("Text: ")
letters = 0
words = 0
sentences = 0

for letter in text:
    if letter.isalpha():
        letters += 1
    elif letter == "?" or letter == "." or letter == "!":
        sentences += 1

words = len(text.split())

# print("letters:", letters)
# print("words:", words)
# print("sentences:", sentences)

L = letters / words * 100
S = sentences / words * 100

index = 0.0588 * L - 0.296 * S - 15.8

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade", round(index))
