def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(text):
    copy_string = text
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    for v in text:
        if v in vowels:
            copy_string = copy_string.replace(v, '')

    return copy_string


if __name__ == "__main__":
    main()
