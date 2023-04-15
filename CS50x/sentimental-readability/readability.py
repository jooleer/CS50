from cs50 import get_string


def get_text():
    text = get_string("Text: ")
    return text


def main():
    # import user text
    text = get_text()

    # count amount of words, sentences etc
    words = 1
    sentences = 0
    letters = 0

    # symbols to determine sentences
    symbols = ["!", "?", "."]

    text_length = len(text)
    for i in range(text_length):
        if text[i] in symbols:
            sentences += 1
        elif text[i] == " ":
            words += 1

    # count amount of letters in text
    letters = text_length - sentences - words

    # formula for grade reading level: 0.0588 * L - 0.296 * S - 15.8
    # L = avg number of letters per 100 words
    # S = number of sentences per 100 words text
    L = (letters / words) * 100
    S = (sentences / words) * 100
    grade = 0.058 * L - 0.296 * S - 15.8
    grade = int(round(grade))

    print(f"Rounded grade: {grade}")
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(grade)}")


main()