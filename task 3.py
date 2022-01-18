text = 'The sunset sets at twelve oclock'
def alphabet_position(text):
    text=text.lower()
    z = []
    x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in text:
        if i not in x:
            continue
        else:
            i = x.index(i) + 1
            z.append(i)
    return " ".join(map(str, z))

print(alphabet_position(text))

x1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x2=' '.join(x1)
print(str(x2))
# def alphabet_position(text):
#     x = text.sorted()
#     for i in text:


x3 = text.lower()
print(x3)


# aksbfbab