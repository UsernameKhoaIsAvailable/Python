n = input("Nhap vao 1 so: ")
n = int(n)
num1 = 1
fibo = [0]
i = 0

while num1 <= n:
    fibo.append(num1)
    num1 = fibo[i] + fibo[i+1]
    i = i + 1
print(fibo)
# print(", ".join(fibo))



