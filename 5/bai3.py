from datetime import timedelta, datetime

def get_timestamp(input_date):
    day = timedelta(days = 1)
    month = month_check(datetime_typ)
    year = year_check(datetime_typ)
    print(datetime.timestamp(input_date))
    print(datetime.timestamp(input_date - day))
    print(datetime.timestamp(input_date + day))
    print(datetime.timestamp(input_date + month))
    print(datetime.timestamp(input_date + year))

def convert_datetime_typ(input_date):
    datetime_typ = datetime.strptime(input_date, '%Y/%m/%d %H:%M:%S')
    return datetime_typ

def month_check(datetime_typ):
    _31_days_month = [1, 3, 5, 7, 8, 10, 12]
    _30_days_month = {4, 6, 9, 11}

    if datetime_typ.month in _31_days_month:
        month = timedelta(days = 31)
    elif datetime_typ.month in _30_days_month:
        month = timedelta(days = 30)
    elif datetime_typ.year % 4 == 0:
        month = timedelta(days = 29)
    else:
        month = timedelta(days = 28)
    
    return month

def year_check(datetime_typ):

    if datetime_typ.year % 4 == 0 and datetime_typ.month == 2:
        year = timedelta(days = 366)
    else:
        year = timedelta(days = 365)

    return year

input_date = input("Ngày: ")
datetime_typ = convert_datetime_typ(input_date)

get_timestamp(datetime_typ)