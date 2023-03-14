shoppinglist = {}


def main():
    grocery()


def grocery():
    while True:
        try:
            item = input().upper()
            global shoppinglist
            if item in shoppinglist:
                shoppinglist[item] += 1
            else:
                shoppinglist[item] = 1
        except EOFError:
            showlist()
            break


def showlist():
    global shoppinglist
    newlist = dict(sorted(shoppinglist.items()))

    for item in newlist:
        print(newlist[item], item)


main()
