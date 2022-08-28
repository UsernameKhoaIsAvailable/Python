content = input('Nhap vao 1 xau: ')
name = input('Nhap ten file: ')

file = open(name, 'w')
file.write(content)
file.close()
