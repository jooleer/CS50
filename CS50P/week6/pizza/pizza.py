import csv
import sys
from tabulate import tabulate


def main():
    # check command-line arugments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CVS file")

    # call get_price with provided csv file argument
    get_price(sys.argv[1])


def get_price(pizza):
    # try to open csv file, it not return error and exit
    try:
        with open(pizza) as data:
            read_data = csv.reader(data, delimiter=",")

            # print out pizza prices with first row being the header
            print(tabulate(read_data, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
