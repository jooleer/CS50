import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    people_data = []
    people_data_length = 0
    with open(sys.argv[1], "r", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for i in reader:
            if reader.line_num == 1:
                people_data += i
                people_data_length = len(people_data)
            else:
                people_data += i

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        sequence = (file.read())

    # TODO: Find longest match of each STR in DNA sequence
    dna_results = []
    for i in range(people_data_length-1):
        result = longest_match(sequence, people_data[i+1])
        dna_results.append(result)

    # TODO: Check database for matching profiles
    matching_counter = people_data_length
    while matching_counter < len(people_data):
        matchcount = 0

        for i in range(people_data_length - 1):
            if (int(dna_results[i]) == int(people_data[matching_counter+i+1])):
                matchcount += 1

            if matchcount == (people_data_length - 1):
                print(people_data[matching_counter])
                sys.exit(0)

        matching_counter += people_data_length

    print("No match")
    sys.exit(0)


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
