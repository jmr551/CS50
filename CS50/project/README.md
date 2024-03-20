# Basic ASCII Encryptor/Decryptor with Seed-Based Randomisation
#### Video Demo:
#### Description:
This project implements a basic cypher/decypher of ASCII text as input, using a seed as a key in order to generate random numbers that will be the delta that will cypher or decypher the text for each character, and then it will produce a textfile as the output.

## How does it work?
The idea of this code, written in C, was inspired in the Caesar cipher, but insted of using a constant key, I propose to use a variable one, using the key as the seed of the pseudo-random numbers and adding (or substracting) the value of `rand()` to every ASCII character in order to encrypt (or decrypt) a text file.

Since not every ASCII character could be read by a text editor, I propose to use just the ASCII characters that can be seen (This arbitrary decision, added to the randomness added to the characters, favors the difficulty for an attacker to know how to decrypt the file).

In order to do so, I propose the

## Limitations
I know this is not the safest encription that exists and that there are a lot of algorithms there that are better that this, but I'm this algorithm can be used as a way to learn and practise programming or just for fun. I know that the principle of a secure algorithm is that the code is open but even though it is very hard to decypher the file if you do not have the key.

