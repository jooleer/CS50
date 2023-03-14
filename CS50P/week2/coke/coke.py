def main():
    price = 50
    print("Amount Due: ", price)
    coins = input("Insert Coin: ")
    calculate_change(coins, price)


def calculate_change(coins, price):
    valid_coins = [5, 10, 25]
    if int(coins) in valid_coins:
        price = price - int(coins)

        if price > 0:
            print("Amount Due:", price)
            coins = input("Insert Coin: ")
            calculate_change(coins, price)

        else:
            print(price)
            print("Change Owed:", price * -1)

    else:
        print("Amount Due:", price)
        coins = input("Insert Coin: ")
        calculate_change(coins, price)


main()
