nameInput = input("Nhap vao day ten cach nhau bang dau phay: ")
name = input("Nhap vao ten can dem: ")

nameList = nameInput.split(",")
numOfName = 0

for fullname in nameList:
    nameParts = fullname.split(" ")
    if name == nameParts[-1]:
        numOfName += 1



print(numOfName)