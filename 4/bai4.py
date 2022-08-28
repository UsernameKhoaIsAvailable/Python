original_location = input('Đường dẫn gốc: ')
copied_location = input('Đường dẫn đích: ')
original_location_splited = original_location.split('\\')
file_name = original_location_splited[-1]

try:
    original_file = open(original_location, 'rb')
    copied_file = open(copied_location + file_name, 'wb')
    copied_file.write(original_file.read())
    original_file.close()
    copied_file.close()
except Exception as e:
    print(e)
    print('Lỗi copy file.')