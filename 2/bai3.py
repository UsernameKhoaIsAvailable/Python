str1 = input("Nhap vao 1 xau: ")
str2 = input("Nhap vao 1 xau nua: ")
str1 = str1.lower()
str2 = str2.lower()

# if str1 in str2 or str2 in str1:
#     print("True")
# else:
#     print("False")

print(str1 in str2 or str2 in str1)