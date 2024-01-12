name = input("WHAT IS YOUR NAME? ")
print("HELLO, {}!".format(name.upper()))
num_letters = len(name)
print("YOUR NAME HAS {} LETTER{} IN IT! AWESOME!".format(num_letters, 'S' if num_letters != 1 else ''))
