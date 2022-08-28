# Nhap vao tu ban phim 1 day so tu nhien, cach nhau bang dau phay.
# Tinh tong day so tu nhien do

a=input('Nhap vao tu ban phim 1 day so tu nhien, cach nhau bang dau phay: ')
splitted = a.split(',')
print(splitted)
sum = 0
for b in splitted:
    b= b.strip()
    if b == "":
        continue
    sum = sum + int(b)
print(sum)