import sys
import os


def main():
    # check amount of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")

    # check if file exists and if it's a .py file
    if not os.path.isfile(sys.argv[1]) or not sys.argv[1].endswith(".py"):
        sys.exit("not ok")

    # call count lines function
    count_lines(sys.argv[1])


def count_lines(file):
    lines_amount = 0
    lines = 0

    # open .py file as pf
    with open(file, 'r') as pf:
        lines = pf.readlines()

    # loop through lines
    for line in lines:
        # remove all white spaces
        line = line.replace(" ", "")
        # check if line isn't a comment and not empty
        if not line.startswith("#") and line.strip():
            lines_amount += 1

    # output amount of lines of code
    print(lines_amount)


if __name__ == "__main__":
    main()
