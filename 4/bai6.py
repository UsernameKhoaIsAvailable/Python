import os
_str = input('Nhập vào 1 xâu: ')
is_exist = os.path.exists('Storage.txt')

if is_exist:
    file = open('Storage.txt', 'a')
    file.write('\n' + _str)
    file.close()
else:
    file = open('Storage.txt', 'a')
    file.write(_str)
    file.close()

file = open('Storage.txt', 'r')
print(file.read())
file.close()

file_del = input("Do you want to reset(Y/n): ")
file_del = file_del.lower()
if file_del != 'n':
    os.remove("Storage.txt")


