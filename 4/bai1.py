# Mở file trong python: file = open("bai1.py")
# r: đọc file, lỗi nếu file ko tồn tại
# a: thêm nội dung vào cuối file, tạo file nếu ko tồn tại
# w: ghi đè file, tạo file nếu ko tồn tại
# x: tạo file, lỗi nếu file tồn tại
# t: text mode
# b: bỉnary mode
# relative path: chỉ ra đường dẫn liên quan đến cwd, dùng dấu '.' và '..'
# absolute path: chỉ ra đường dẫn xác định từ root directory
# cwd: thư mục mà đang đc đọc, viết,...

import os
print("Current working directory:", os.getcwd())