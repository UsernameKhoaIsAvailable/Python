while True:
    numstr = input("Nhap vao 1 day so: ")
    numlist = numstr.split(',')
    sum = 0

    try:
        for number in numlist:
            sum += int(number)
        print(sum)
        break

    except:
        pass