import os

def query():
    key = input('Key: ')

    try:
        file = open('Data/' + key, 'r')
        print(file.read())
        file.close()
    except:
        print('Không tìm thấy!')

def add():
    key = input('Key: ')
    value = input('Value: ')

    if os.path.exists('Data/' + key):
        print('Key đã tồn tại!')
    else:
        file = open('Data/' + key, 'w')
        file.write(value)
        file.close()

def delete():
    key = input('Key: ')

    if os.path.exists('Data/' + key):
        os.remove('Data/' + key)
        print('Đã xóa!')
    else:
        print('Không tìm thấy!')

def edit():
    key = input('Key: ')

    if os.path.exists('Data/' + key):
        value = input('Value: ')
        
        file = open('Data/' + key, 'w')
        file.write(value)
        file.close()
    else:
        print('Không tìm thấy!')

def main():
    try:
        os.mkdir('Data')
    except FileExistsError:
        pass
        
    while True:
        print('1. Truy xuất dữ liệu')
        print('2. Thêm dữ liệu')
        print('3. Xóa dữ liệu')
        print('4. Sửa dữ liệu')
        print('5. Thoát')
        user_choose = input('=> ')

        if user_choose == '1':
            query()
        elif user_choose == '2':
            add()
        elif user_choose == '3':
            delete()
        elif user_choose == '4':
            edit()
        elif user_choose == '5':
            break
        else:
            os.system('cls')        

if __name__ == '__main__':
    main()

       