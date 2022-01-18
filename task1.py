
y = 'this is another sentence'
x = y.split()
print(x)
def spin_words(sentence):
    x = sentence.split()
    for i in x:
        if len(i) > 4:
            x[x.index(i)] = i[::-1]
        else:
            continue
    return ' '.join(x)








print(spin_words(y))
