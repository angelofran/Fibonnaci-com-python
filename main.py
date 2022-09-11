n = int(input("Número de elementos: "))
a = 0
b = 1
s = 0
for _ in range(n):
    print(s, end=" ")
    s = a + b
    b = a
    a = s