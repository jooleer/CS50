import csv
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    if len(sys.argv) > 3:
        print("Too many command-line arguments")

    convert(sys.argv[1], sys.argv[2])


def convert(input, output):
    out = open(output, "w")
    try:
        with open(input) as file:
            file_reader = csv.reader(file, delimiter=",")
            for line in file_reader:
                print(line)
    except FileNotFoundError:
        print("Could not read", input)
        sys.exit()



if __name__ == "__main__":
    main()
