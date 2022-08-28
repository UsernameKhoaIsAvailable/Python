import os


while True:
    print('1. Truy xuất dữ liệu')
    print('2. Thêm dữ liệu')
    print('3. Xóa dữ liệu')
    print('4. Sửa dữ liệu')
    user_choose = input('=> ')

    if user_choose == '1':
        key = input('Key: ')

        try:
            file = open(key, 'r')
            print(file.read())
            file.close()
        except:
            print('Không tìm thấy!')

    elif user_choose == '2':
        key = input('Key: ')
        value = input('Value: ')

        if os.path.exists(key):
            print('Key đã tồn tại!')
        else:
            file = open(key, 'w')
            file.write(value)
            file.close()
        
    elif user_choose == '3':
        key = input('Key: ')

        if os.path.exists(key):
            os.remove(key)
            print('Đã xóa!')
        else:
            print('Không tìm thấy!')

    elif user_choose == '4':
        key = input('Key: ')

        if os.path.exists(key):
            value = input('Value: ')
            
            file = open(key, 'w')
            file.write(value)
            file.close()
        else:
            print('Không tìm thấy!')

    else:
        os.system('cls')
        continue

