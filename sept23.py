names = ['a', 'b', 'c']
amounts = [1, 2, 3]

def max():
    max = amounts[0]
    for i, j in enumerate(amounts):
        if j > max:
            max = j
            name = names[i]
    return name

print(max())