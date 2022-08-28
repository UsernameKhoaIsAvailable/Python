person1 = {
    "tên": "Khoa",
    "tuổi": "18",
    "địa chỉ": "Mipec City View",
    "số điện thoại": "0123456789",
}

person2 = {
    "tên": "Khoa",
    "tuổi": "2",
    "địa chỉ": "Mipec City View",
    "số điện thoại": "000000",
}

def compare(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            if value != dict1[key]:
                print(f"{key}: {value} & {dict1[key]}")

compare(person1, person2)
