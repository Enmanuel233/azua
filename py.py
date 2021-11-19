
def azua(string1):
    j = []
    for i in string1:
        if i == '0':
            j.append(i)
            x = j.count(i)
    return x

print(azua('11100000111000'))

print(azua('5000478'))