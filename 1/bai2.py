N = input("Nhap vao 1 so tu nhien: ")
N = int(N)
odd = 0
even = 0
i = 1
result = 10

while int(result/10) != 0:
    result = int(N/i)
    if result%2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i * 10

if even == odd:
    print("N =", N, "la so can bang")   
else:
    print("N =", N, "khong la so can bang")   

