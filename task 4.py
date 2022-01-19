x = int(input('Размер вашего депозта'))
y = 0.05
range = int(input('расчетное движение'))
def lot(dep, risk, range):
    dep = dep
    risk = risk
    range = range
    loss = dep*risk
    return loss/range

print(lot(x,y,range))