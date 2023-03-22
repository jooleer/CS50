import re


def main():
    print(count(input("Text: ")))


def count(s):
    # return length of list returned by checking s for regex Um/um
    return len(re.findall(r"\b[U-u]m\b", s))


if __name__ == "__main__":
    main()
