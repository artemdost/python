def translate(x, i):
    x1 = int(x)
    x2 = x % 1
    s1 = ''
    s2 = ''
    while x1 > 0:
        s1 = str(x1 % i) + s1
        x1 = x1 // i
    if i == 2:
        for j in range(n):
            x2 = x2 * 2
            if x2 > 1:
                s2 += '1'
                x2 = x2 % 1
            elif x2 == 1:
                s2 += '1'
                break
            else:
                s2 += '0'
    if i == 8:
        for j in range(n):
            x2 = x2 * 8
            if x2 > 1:
                s2 += str(int(x2))
                x2 = x2 % 1
            elif x2 == int(x2):
                s2 += str(int(x2))
                break
            else:
                s2 += '0'
    s = s1 +'.' + s2
    print("Число после перевода:", float(s))
        
    
x = float(input("Введите число: "))
n = int(input("Введите кол-во знаков после запятой: "))
i = int(input("Укажите систему счисления, в которую осуществить перевод (2 или 8): "))
translate(x,i)