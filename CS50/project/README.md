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
#### My example
```
./secreto enc 12345 archivo_entrada.txt archivo_salida.txt
./secreto dec 12345 archivo_salida.txt recuperado.txt
```
#### General example
```
./secreto enc 12345 input_file.txt output_file.txt
./secreto dec 12345 output_file.txt recovered.txt
```

And recuperado.txt should be the same as archivo_entrada.txt.

### Example
- Input File:
```
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
```

- Output File:
```
p7eT$H#y*@@TBF<LdC0}7',pkVMm;k+n`[*o:g;z P2Upm;pu e+~Xz[)FdC}r:@+X1b%8Q,|h_`Oe@4OdYW_6~jSNASH!)3O.W:@}^@]&}_2=;!}$E{2JNoq8AUQ6tT?/~PJMPm8RpC}x?mz)+mox\IsylC$"/?M-:v{ckG5DdK~O'~JJ#g";Q(EHmDKGzp7'TbPS(8tjr{v &S,]N"C8gB7+?jI3C%duV&@HV;@h5RXx~L~#'6V7{sC9I&_lj&$B/76\JN(N0ja<Xc+,4y W/O1x?}!$b7MdgAL[}#e+l}Y8jr?`NRdQ,ulBV<G$u%j6r//$62:u!{[[hpe"E(\K"2Sx+h%8[P/'y="\t,z<dWdO>?J$UwC[U[v2B|,l&,.R%&E+R*Cz}IUqv(_ueH^~<%1z/zH1Dp/%yB~RdP5ei'mzX[d-ODm9VjHDfKxNi'6,yGtkk\BDh|:O}BUhY)V/d<TV*0DLN[<Z:Q8ZEmj!YtAS-_7 xU?TpG|p{P`O(|$C` Ju^KxGE:eIxx=x]7?G|RY44$ M5(Lt7<;X_4Ic%%N/X-qSwk|P}p40pXBo.v!:>pld<TUA`k?GV ~J_eJEH_j1#z/8UP5):28K~bZS^=m!8WVg>dJSP{sT_?h?Q7EbXL2IDxvbAOurXL3z:d`cv,/+f-g!?$w`~>s28pA}uxT90K@wx+PC@=#wQjYvN2eoI!#lQ?ff$rd.}<? FK/t!e$YfnUb%=IJhFFRe#v}&bp7*K}6'nPswTiOJI6pj~w#Mi=*A12|/F*}7?R`A<yP59?NYL~DM?^3g=Y.x/n]8BI~"JkF7FFzu(?HbYQ%.,#Jz[l#=uIK]sMD &V?LD3?HU;/KHgNh%Ju^Dylb~zDLGi1S)e~)x?sTXf, A*/3F(D4'>|5/1]LeB))@-Q/E:#q5]$Ot)a<:|FAg63yPYgR4aiHzs_2>K@B,4{-L=HV,Q[2g:l,v@^~="ns?Y&I&@-oW.$63TiSm?RS.6f#t/=,H,~ Upff9`Pv^L}vS]=1P\\,48u!c?['ZK1q=W:JHmA2uA8;mI_XK|oDLiX}$t7I5(=_%%%*KT?Y(p(!.#FgF0wceV]$(~UI*mC^o<y+jD8\$.^L!0E&_GA88`6eEuvDgrZO:WA'J9/&wJJbhS <mTLG6LJ\);~_F(.'Z_'vza(^"'FZYo#Z&Gz8oKWu\T})8F0-o6rt.ja'aSZdrS,v%5}yZ^?b(\8.:P]>[<Hsm2soVaQrISAcx]TlQ;YfDfOWKFp(o*_`Q;e2;<oiO=Kl#g,MOE}4"g@(,U||jljNQisaOCIbqs*~i60T]51a't~$Anhlh4jx!Zc|BJ9j_V6'`hW'^#,<TZAz:>lDtqFol}+qNcY{;$t$T4+*]6zrLmmrHxr"f7_VC|%DfgL.VK*p*vlaTD8*7:~j^.R<NKgLeG0BzJP5hr;kM.JtzE&BP 6D0O*kD':;K|1Y~d6~w$z|Mxt+)8GxO2A{A}39RGpNL#C_u'>g&&^a<edD**&i:Y]hdp?uKfI% ~l{icO&{:g*++Q)JzlpwVpDI~-n&vm~`9]*N}V%k?Fv.n~T+x][2Ayi =8I+F'x.'!H'R_aLw[s/Ge~?|U>0qwa1NRH|m05\pFsFn~}`Yi7P"SH>2Y{7xJI%<fnTf[5_yEf49:C"eik+=YUZuL^{Yt$PprE(Ps:c!l .5C.tV$+NO@ :X[IZJYu|MH<|J
```


