answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")

replies = ['42', 'forty-two', 'forty two']

if answer.lower().strip() in replies:
    print("Yes")
else:
    print("No")
