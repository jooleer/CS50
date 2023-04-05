def main():
    # optional test variables
    jar = Jar(20)
    print(jar.size)
    print(jar.capacity)
    jar.deposit(15)
    print(jar)
    jar.withdraw(12)
    print(jar)


class Jar:
    def __init__(self, capacity=12):
        # set amount to 0
        self._size = 0

        # check if provided capacity is negative
        if capacity < 0:
            raise ValueError
        #  set capacity
        self._capacity = capacity

    def __str__(self):
        # output one cookie (🍪) for size (amount of cookies)
        return "🍪" * self.size

    def deposit(self, n):
        # check if adding cookies will overload capacity
        if n + self.size > self.capacity:
            raise ValueError

        # add deposit amount to size
        self._size += n

    def withdraw(self, n):
        # check if removing cookies will go below 0
        if n > self.size:
            raise ValueError

        # remove withraw amount from size
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    main()
