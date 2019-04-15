target = [57, 17, 27, 7, 37, 47]
srch = int(input('Value for searching location: '))

flag = 0
for k in range(len(target)): #Annotation ¡÷ºÆ.
    if target[k] == srch:
        print('Searching result: %s' %(k + 1))
        flag = 1
        break

if flag != 1:
    print('Not found: 0')
