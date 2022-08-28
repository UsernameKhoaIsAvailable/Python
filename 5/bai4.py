def day_check(month, year):
    _31_days_month = [1, 3, 5, 7, 8, 10, 12]
    _30_days_month = {4, 6, 9, 11}

    if int(month) in _31_days_month:
        day = '31'
    elif int(month) in _30_days_month:
        day = '30'
    elif int(year) % 4 == 0:
        day = '29'
    else:
        day = '28'
    
    return day

def last_day_of_month(day, month, year):
    date = day + ',' + month + ',' + year
    from datetime import datetime
    f_date = datetime.strptime(date, '%d,%m,%Y')
    print(f_date)

month = input('Tháng: ')
year = input('Năm: ')
day = day_check(month, year)

last_day_of_month(day, month, year)
