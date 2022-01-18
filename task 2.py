
x = [1, 2, 'aasf','alba', 2 , '2', '4','10','7', '8', 123]
for i in x:
    print(type(i))

def ala(l):
    for i in l:
        if type(i)==str:
            l.remove(i)
        else:
            continue
    return l
print(ala(x))

print('hi')
git init



























#solution
# def filter_list(l):
#     x = []
#     for i in l:
#         if type(i) == int:
#             x.append(i)
#         else:
#             continue
#     return x
# print(filter_list(x))

