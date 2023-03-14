def main():
    menu()


def menu():
    price = 0
    while True:
        try:
            menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }

            item = input("Item: ")
            price += menu[item.title()]
            print("Price: ${:0.2f}".format(price))
        except EOFError:
            break
        except KeyError:
            pass


main()
