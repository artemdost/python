n = int(input("Укажите размерность массива: "))
m = [0] * n
print("Введите", n, "чисел / числа: ")
index = 100000
mmax = -1000000000
for i in range(n):
    m[i] = float(input())
    if m[i] > mmax:
        mmax = m[i]
        index = i
for i in range(index+1, n):
    m[i] = float(0)
print(*m)

