n = int(input("Укажите размерность массива: "))
d = int(input("Укажите значение delta: "))
m = [0] * n
print("Введите", n, "значений: ")
mmin = 10 ** 100
for i in range(n):
    m[i] = int(input())
    if m[i] < mmin:
        mmin = m[i]
k = 0
for i in m:
    if i - mmin == d:
        k += 1
print("Количество элементов:", k)
    
