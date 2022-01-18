x ="Dermatoglyphics"
x1 ="aba"
x2 = "moOse"


def huynia(text):
    text = text.lower()
    def calc(text):
        text=text.lower()
        l = []
        for i in text:
            if text.count(i)>1:
                l.append(0)
            else:
                l.append(1)
        return sum(l)
    if text.__len__() == calc(text):
        return True
    else:
        return False
huynia(x2)