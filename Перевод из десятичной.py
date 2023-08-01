def non_des(numeral):
    numeral -= 10
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(abc)):
        if numeral == i:
            return abc[i]
n = int(input('Число в десятеричной системе: '))
s = int(input('Система счисления: '))
spisok = []
celoe = 1000
while celoe >= s:
    celoe = n // s
    ostatok = n % s
    spisok.append(ostatok)
    n = celoe
spisok.append(celoe)
spisok.reverse()
for i in spisok:
    if i > 9:
        ind = spisok.index(i)
        new = non_des(i)
        spisok.remove(i)
        spisok.insert(ind, new)
print(*spisok, sep='')