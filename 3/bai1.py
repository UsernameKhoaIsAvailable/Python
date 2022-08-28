class Person():
    def __init__(self, name, age, gender, mobile_phone, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile_phone = mobile_phone
        self.address = address

    def say_hello(self):
        print('Hello')

    def move_home(self):
        new_address = input('Enter new address: ')
        self.address = new_address

    def call(self, other_person):
        print('Calling', other_person.name)

person1 = Person('Hin', 3, 'male', '012345678', 'Mipec')
person2 = Person('Ti', 23, 'male', '87654321', 'Van Cao')

person1.say_hello()
person2.move_home()
person1.call(person2)

