numbers = input("Nhap vao 1 day so tu nhien: ")
numbers = numbers.split()
if min(numbers) == max(numbers):
    print("Khong co so lon nhat, nho nhat")
else:
    print("So nho nhat: ", min(numbers))
    print("So lon nhat: ", max(numbers))


