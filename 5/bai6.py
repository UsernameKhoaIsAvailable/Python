from datetime import datetime, timedelta

def convert_datetime_typ(input_date):
    datetime_typ = datetime.strptime(input_date, '%d/%m/%Y')
    return datetime_typ

def main():
    date1 = input('Ngày tháng năm (dd/mm/yyyy): ' )
    date2 = input('Ngày tháng năm (dd/mm/yyyy): ' )

    date1_datetime_typ = convert_datetime_typ(date1)
    date2_datetime_typ = convert_datetime_typ(date2)

    print('Hiệu số ngày:', abs(date1_datetime_typ - date2_datetime_typ).days)

if __name__ == '__main__':
    main()
