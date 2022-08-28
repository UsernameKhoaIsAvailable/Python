import os

def choose_1(user_choose):
    if user_choose == '1':
        key = input('Key: ')

        try:
            file = open(key, 'r')
            print(file.read())
            file.close()
        except:
            print('Không tìm thấy!')

def choose_2(user_choose):
    if user_choose == '2':
        key = input('Key: ')
        value = input('Value: ')

        if os.path.exists(key):
            print('Key đã tồn tại!')
        else:
            file = open(key, 'w')
            file.write(value)
            file.close()

def choose_3(user_choose):
    if user_choose == '3':
        key = input('Key: ')

        if os.path.exists(key):
            os.remove(key)
            print('Đã xóa!')
        else:
            print('Không tìm thấy!')

def choose_4(user_choose):
    if user_choose == '4':
        key = input('Key: ')

        if os.path.exists(key):
            value = input('Value: ')
            
            file = open(key, 'w')
            file.write(value)
            file.close()
        else:
            print('Không tìm thấy!')

def choose_5(user_choose):
    if user_choose == '5':
        return False
    else:
        return True

def other_choose(user_choose):
    choose = ['1', '2', '3', '4', '5']
    if user_choose not in choose:
        os.system('cls')

def main():    
    _bool = True
    while _bool :
        print('1. Truy xuất dữ liệu')
        print('2. Thêm dữ liệu')
        print('3. Xóa dữ liệu')
        print('4. Sửa dữ liệu')
        print('5. Thoát')
        user_choose = input('=> ')

        choose_1(user_choose)
        choose_2(user_choose)
        choose_3(user_choose)
        choose_4(user_choose)
        _bool = choose_5(user_choose)
        other_choose(user_choose)
        continue

if __name__ == '__main__':
    main()