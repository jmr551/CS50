# Basic ASCII Encryptor/Decryptor with Seed-Based Randomisation
#### Video Demo:
#### Description:
This project implements a basic cypher/decypher of ASCII text as input, using a seed as a key in order to generate random numbers that will be the delta that will cypher or decypher the text for each character, and then it will produce a textfile as the output.

## How does it work?
The idea of this code, written in C, was inspired in the Caesar cipher, but insted of using a constant key, I propose to use a variable one, using the key as the seed of the pseudo-random numbers and adding (or substracting) the value of `rand()` to every ASCII character in order to encrypt (or decrypt) a text file.

Since not every ASCII character could be read by a text editor, I propose to use just the ASCII characters that can be seen (This arbitrary decision, added to the randomness added to the characters, favors the difficulty for an attacker to know how to decrypt the file).

The characters that could be read are in the range from 32 to 126. So the delta should be in this range:
`int delta = rand() % (127 - 32);`
So, I read every character from the text file, obtain the corresponding delta and add to the ASCII character.
But, in order to avoid overflow, the result needs to be circular, that is if the result is, for example, 128, that should map to 32, 129 to 33 and so on. I can get that by doing this:
`res = ((c - 32 + delta) % (127 - 32)) + 32;`
So, I substract 32 (like zeroing), I add the corresponding delta.

## Limitations
I know this is not the safest encription that exists and that there are a lot of algorithms there that are better that this, but I'm this algorithm can be used as a way to learn and practise programming or just for fun. I know that the principle of a secure algorithm is that the code is open but even though it is very hard to decypher the file if you do not have the key. So the conclusion is that this algorithm relies on the secrecy of the idea of the algoritm (and a bit in the key xD).

## How to Execute
1. Compile the program:
```
gcc -o secreto secreto.c
```
2. Run the program
- To encrypt a file:
```
./secreto enc <key> <input_file> <output_file>
```

- To decrypt a file:
```
./secreto dec <key> <input_file> <output_file>
```

### Use Example
```
./secreto enc 12345 archivo_entrada.txt archivo_salida.txt
./secreto dec 12345 archivo_salida.txt recuperado.txt
```

And recuperado.txt should be the same as archivo_entrada.txt.

### Example
- Input File:
```
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
```

- Output File:


