# Basic ASCII Encryptor/Decryptor with Seed-Based Randomisation
#### Video Demo:
#### Description:
This project implements a basic cypher/decypher of ASCII text as input, using a seed as a key in order to generate random numbers that will be the delta that will cypher or decypher the text for each character, and then it will produce a textfile as the output.

## How does it work?
This code is written in C and uses the `rand()` function from the C standard library.
The seed is initialised with the key provided by the user through command line.
This algorithm is inspired in the Caesar cipher
