import sys


def main():
    gather_names()


def gather_names():
    greetings = []
    
    # make a loop that keeps asking user for names until ctrl-d is pressed
    while True:
        try:
            name = input("Name: ")
            greetings.append(name)
        except EOFError:
            break

    # send names in the list to print function
    print_names(greetings)


# print names in provided list
def print_names(names):
    message = ""

    # no names provided
    if len(names) == 0:
        sys.exit()

    # 1 name in list
    if len(names) == 1:
        message = names[0]

    # 2 names in list
    elif len(names) == 2:
        message = names[0] + " and " + names[1]

    # if more than 3 names in list
    else:
        count = 0
        for name in names:
            if count == 0:
                message = name
                count += 1
            elif count < len(names) - 1:
                message = message + ", " + name
                count += 1
            else:
                message = message + ", and " + name
                count += 1

    # print out names
    print("\nAdieu, adieu, to " + message)


main()
