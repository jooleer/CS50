def main():
    text = input("Input: ")
    remove_vowels(text)


def remove_vowels(text):
    copy_string = text
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    for v in text:
        if v in vowels:
            copy_string = copy_string.replace(v, '')

    print("Output:", copy_string)


main()
