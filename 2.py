from random import randint


n1 = int(input("Укажите размерность массива A: "))
n2 = int(input("Укажите размерность массива B: "))
A = [0] * n1
B = [0] * n2
for i in range(n1):
    A[i] = randint(-10, 10)
for i in range(n2):
    B[i] = randint(-10, 10)
print(A,B)
for i in A:
    if i in B:
        print(i)
    
