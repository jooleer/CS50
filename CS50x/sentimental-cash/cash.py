# import function from cs50
from cs50 import get_float


def main():
    money = change()
    money = round(money, 2)
    print(f"Money: {money}")
    currency = 0

    print(f"Money owed: {money}")
    while money >= 0.01:
        while money >= 0.05:
            while money >= 0.1:
                while money >= 0.25:
                    money = round(money, 2)
                    if money >= 0.25:
                        currency += 1
                        money -= 0.25
                        # print("1 x 0.25")
                money = round(money, 2)
                if money >= 0.1:
                    currency += 1
                    money -= 0.1
                    # print("1 x 0.1")
                    # print(f"money: {money}")
            money = round(money, 2)
            if money >= 0.05:
                currency += 1
                money -= 0.05
                # print("1 x 0.05")
        money = round(money, 2)
        if money >= 0.01:
            currency += 1
            money -= 0.01
            # print("1 x 0.01")

    print(f"{currency}")


def change():
    while True:
        try:
            n = get_float("Change owed: ")
        except ValueError:
            print("Incorrect input.")
        else:
            if n > 0:
                return n


main()

