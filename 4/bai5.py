location = input('Nhập vào 1 đường dẫn: ')
file = open(location, 'r')
print(len(file.readlines()))
file.close()