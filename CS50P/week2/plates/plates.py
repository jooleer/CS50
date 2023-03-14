def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # verification

    # check length
    if len(s) < 2 or len(s) > 6:
        return False

    # check for any non-alphanumeric characters
    if s.isalnum() is False:
        return False

    # check if there is no leading 0 if there's any numbers
    if s[0:1].isalpha():
        if len(s) >= 4:
            if s[len(s)-2:len(s)-1].isnumeric():
                if s[len(s)-2] == '0':
                    return False

    # check if a letter comes after numbers
    for char in range(len(s)):
        if char == len(s)-1:
            break
        if s[char].isnumeric():
            if s[char+1].isalpha():
                return False

    # if all checks turn out to be false, our plate should be valid
    return True


main()
