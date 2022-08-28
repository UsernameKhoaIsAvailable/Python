a = 5 # int
b = 1.2 # float
c = "abcdef" # str
c = "a" # str

# int a = 4;
a = 4
# a = "abcdef"

# print(a)
# print(b)

# a = input("Nhap vao mot so: ")
# b = input("Nhap vao so nua: ")

# c = int(a) + int(b)
# print(c)

if a > 5:
    print("A lon hon 5")
elif a >3:
    print("A lon hon 3")
else:
    print("A be hon")


# for i in range(9, 0, -2):
#     print(i)

# i = 0
# while i < 5:
#     i += 1
# print(i)

a = list()
a = []
a = [1, 3, 4, 5, 1, 2, 3, 5]
# print(a)

# print(a[1])
# print(a[0:2])
# print(a[:2])

# print(a[2:6])

# print(a[0:7:2])
# print(a[:7:2])

# print(a[7::-1])

# print(a[2:])

# b = a[:7:2]

a.append("acsb")
print(a)

# a[5] = 'hello'
# print(a)

# print(a.count(1))

# print(len(a))

# a.remove(1)
# print(a)

# last_element = a.pop(3)
# print(last_element)
# print(a)

# print("Noi mang")
# a = ["acb", "123", "445", "kacmslac"]
# print(", ".join(a))

# _dict = {}
# _dict = dict()

# _dict["ten"] = "Hin"
# _dict["tuoi"] = 2

# print(_dict)
# print(_dict["tuoi"])

# thong_tin_hoc_sinh = dict()
# thong_tin_hoc_sinh["ten"] = "Khoa"
# thong_tin_hoc_sinh["tuoi"] = "2"
# thong_tin_hoc_sinh["lop"] = "Vo hoc"
# thong_tin_hoc_sinh["nghe nghiep"] = "That nghiep"

# print(thong_tin_hoc_sinh)

# thong_tin_lop_hoc = {
#     "Tran Minh Khoa": {
#         "ten": "Khoa",
#         "tuoi": 2
#     },
#     "Sang": {
#         "ten": "Sang",
#         "tuoi": 18,
#     }
# }


# # Ten day du, Ten, Tuoi
# # Tran Minh Khoa, Khoa, 2
# # Sang, Sang, 18

# user_input = input("Nhap vao 1 day so tu nhien cach nhau bang dau cach: ")
# splitted = user_input.split(" ")
# print(splitted)
# print(type(splitted))

# def ten_ham(arg1, arg2):
#     print(arg1 + arg2)
#     print(0)

# ten_ham(1, 2)

def tinh_tong(so1, so2):
    # so1 + so2
    return so1 + so2


1 + 2

ket_qua = 0
ket_qua = tinh_tong(1, 2)
print(ket_qua)