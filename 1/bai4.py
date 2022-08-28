import random
import os
print("Chao mung ban den voi tro choi oan tu ti.")
score = 0
comScore = 0
o = 0
_continue = 'a'
while _continue != 'k':
    print("Hay chon:")
    print("1. Dam")
    print("2. La")
    print("3. Keo")
    choose = input("Lua chon cua ban: ")
    choose = int(choose)
    comChoose = random.randint(1,3)
    if choose == 1:
        print("Ban da chon: Dam")
        if comChoose == 2:
            print("May tinh chon: La")
            o = 1
        if comChoose == 3:
            print('May tinh chon: Keo')

    elif choose == 2:
        print("Ban da chon: La")
        if comChoose == 1:
            print('May tinh chon: Dam')
        if comChoose == 3:
            print('May tinh chon: Keo')
            o = 1

    elif choose == 3:
        print("Ban da chon: Keo")
        if comChoose == 1:
            print('May tinh chon: Dam')
            o = 1
        if comChoose == 2:
            print("May tinh chon: La")

    else:
        os.system('cls')
        continue

    if choose == comChoose:
        print(f'Hoa! Ti so (May-Nguoi): {comScore}-{score}')
    else:
        if o == 0:
            score += 1
            print(f'Ban da thang! Ti so (May-Nguoi): {comScore}-{score}')
        else:
            comScore += 1
            print(f'Ban da thua! Ti so (May-Nguoi): {comScore}-{score}')
    
    _continue = input("Tiep tuc (.../K)?")
    _continue = _continue.lower()

    if _continue == 'k':
        score = 0
        comScore = 0
    


        