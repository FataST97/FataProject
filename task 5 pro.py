def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


x ="Dermatoglyphics"
x1 ="aba"
x2 = "moOse"

print(is_isogram(x1))