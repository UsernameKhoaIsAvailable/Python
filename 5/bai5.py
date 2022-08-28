from datetime import datetime


def convert_datetime_typ(input_date):
    datetime_typ = datetime.strptime(input_date, '%Y/%m/%d')
    return datetime_typ

def age_calculate(datetime_typ):
    age = datetime.now().year - datetime_typ.year
    if age == 0:
        age = datetime.now().month - datetime_typ.month
        print('Tuổi:', age, 'tháng')
    else:
        print('Tuổi:', age)

birthday = input("Ngày sinh: ")
datetime_typ = convert_datetime_typ(birthday)
age_calculate(datetime_typ)