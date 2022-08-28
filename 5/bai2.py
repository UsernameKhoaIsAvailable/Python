def convert(full_day):
    from datetime import datetime
    datetime_typ = datetime.strptime(full_day, '%b %d %Y %I:%M %p')
    datetime_str = datetime_typ.strftime('%Y/%m/%d %H:%M:%S')
    print(datetime_str)

full_day = input("Ngày: ")
convert(full_day)