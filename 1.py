n = int(input("Укажите размерность массива: "))
m = [0] * n
print("Введите", n, "чисел / числа: ")
mmax = -100000000
for i in range(n):
    m[i] = float(input())
    if m[i] > mmax:
        mmax = m[i]
    else:
        m[i] = float(0)
print(*m)
