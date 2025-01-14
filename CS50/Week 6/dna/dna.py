import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py <DATABASE_ADDRESS>.csv <SEQUENCE_ADDRESS>.txt")
        return 1

    # TODO: Read database file into a variable
    lista = []
    with open(sys.argv[1]) as my_file:
        data = csv.reader(my_file)
        for row in data:
            lista.append(row)
    data = []

    for i in range(1, len(lista)):
        tmp_dict = {}
        for j in range(0, len(lista[0])):
            tmp_dict[lista[0][j]] = lista[i][j]
        data.append(tmp_dict)
    gen_seqs = list(data[0].keys())
    gen_seqs.remove("name")

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as my_file:
        sequence = my_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    unknown_person = {}
    for seq in gen_seqs:
        unknown_person[seq] = longest_match(sequence, seq)

    # TODO: Check database for matching profiles
    for person in data:
        same = True
        for seq in gen_seqs:
            if int(person[seq]) != unknown_person[seq]:
                same = False
        if same:
            print(person["name"])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
