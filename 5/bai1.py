from datetime import datetime
now = datetime.now()
print('Ngày tháng năm, giờ phút giây hiện tại:', now)
print('Năm hiện tại:', now.year)
print('Tháng hiện tại:', now.month)
print('Hiện tại là tuần thứ', now.strftime('%U'), 'trong năm')
print('Today is', now.strftime('%A'))
print('Hôm nay là ngày thứ', now.strftime('%j'), 'trong năm:')
print('Hôm nay là ngày', now.strftime('%d'), 'trong tháng:')