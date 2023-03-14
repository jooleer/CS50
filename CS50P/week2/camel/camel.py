def main():
    v = input("camelCase: ")
    to_snake(v)


def to_snake(input):
    input_list = list(input)
    for i in range(len(input)):
        if input[i].isupper():
            input_list[i] = "_" + input[i].lower()
    print("snake_case: " + "".join(input_list))


main()
