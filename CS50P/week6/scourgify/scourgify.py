import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # send command-line arguments to convert function
    convert(sys.argv[1], sys.argv[2])


def convert(input, output):
    # open output file and write first/header row
    out = open(output, "w")
    writer = csv.writer(out)
    header_row = ["first", "last", "house"]
    writer.writerow(header_row)

    # open input file, read and convert each line, and write to output
    try:
        with open(input) as file:
            file_reader = csv.reader(file, delimiter=",")
            for line in file_reader:
                try:
                    name = line[0].split(",")
                    row = name[1].strip(), name[0], line[1]
                    writer.writerow(row)

                # handle header line (less than 3 values)
                except IndexError:
                    pass

    # input file doesnt exist, print error and exit
    except FileNotFoundError:
        print("Could not read", input)
        sys.exit(1)

    # close output file
    out.close()


if __name__ == "__main__":
    main()
