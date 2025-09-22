values = [0, 2, 4, 6, 8, 10]

counter = 0
while counter != 10:
    string = 'hello'
    if counter in values:
        string = string + ' world'
    print(string)
    counter += 1

memory = ' world'
print(string + memory)