def funct(n):
    m = [0] * n
    print("Введите", n, "чисел / числа: ")
    index = 100000
    mmax = -100000000
    for i in range(n):
        m[i] = float(input())
        if m[i] > mmax:
            mmax = m[i]
            index = i
    for i in range(index+1, n):
        m[i] = float(0)
    print(*m)
    
n = int(input("Укажите размерность массива: "))
funct(n)

