def main():
    print("$", value(input("Greeting: ")))


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()
