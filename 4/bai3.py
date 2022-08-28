from xml.dom import ValidationErr


location = input('Nhap vao duong dan: ')

try:
    file = open(location, 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('File không tồn tại')
