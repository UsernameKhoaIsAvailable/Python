from linked_list import LinkedList


class EmptyAnimalShelterException(Exception):
    pass


class AnimalShelter:
    def __init__(self):
        self.dog_shelter = LinkedList()
        self.cat_shelter = LinkedList()

    def enqueue(self, animal_type, name):
        new_data = {
            'type': animal_type,
            'name': name,
            'number': 0
        }

        if animal_type == 'dog':
            self.dog_shelter.add(new_data)
        else:
            self.cat_shelter.add(new_data)

        new_data['number'] = self.dog_shelter.length + self.cat_shelter.length

    def dequeue_any(self):
        if self.dog_shelter.length + self.cat_shelter.length == 0:
            raise EmptyAnimalShelterException

        if self.dog_shelter.head.data['number'] == 1:
            return_animal = self.dog_shelter.head
            self.dog_shelter.remove_at(0)
        else:
            return_animal = self.cat_shelter.head
            self.cat_shelter.remove_at(0)

        rearrange_dogs_cats_order(self)
        return f"{return_animal.data['name']} the {return_animal.data['type']}"

    def dequeue_dog(self):
        if self.dog_shelter.length == 0:
            raise EmptyAnimalShelterException

        return_animal = self.dog_shelter.head
        self.dog_shelter.remove_at(0)
        rearrange_dogs_cats_order(self)

        return f"{return_animal.data['name']} the {return_animal.data['type']}"

    def dequeue_cat(self):
        if self.cat_shelter.length == 0:
            raise EmptyAnimalShelterException

        return_animal = self.cat_shelter.head
        self.cat_shelter.remove_at(0)
        rearrange_dogs_cats_order(self)

        return f"{return_animal.data['name']} the {return_animal.data['type']}"

    def __str__(self):
        if self.dog_shelter.head.data['number'] == 1:
            current_node = self.dog_shelter.head
            temp_node = self.cat_shelter.head
        else:
            current_node = self.cat_shelter.head
            temp_node = self.dog_shelter.head

        return_str = ''
        i = 0

        while i != self.dog_shelter.length + self.cat_shelter.length:
            return_str += current_node.data['name']
            return_str += ' the '
            return_str += current_node.data['type']

            if i != self.dog_shelter.length + self.cat_shelter.length - 1:
                return_str += ', '

            try:
                if current_node.next.data['number'] == current_node.data['number'] + 1:
                    current_node = current_node.next
                else:
                    temp_node2 = current_node.next
                    current_node = temp_node
                    temp_node = temp_node2
            except AttributeError:
                current_node = temp_node

            i += 1

        return return_str


def rearrange_dogs_cats_order(_list: AnimalShelter):
    current_node1 = _list.dog_shelter.head

    if _list.dog_shelter.head.data['number'] == 1:
        current_node1 = current_node1.next

    current_node2 = _list.cat_shelter.head

    if _list.cat_shelter.head.data['number'] == 1:
        current_node2 = current_node2.next

    while current_node1:
        current_node1.data['number'] -= 1
        current_node1 = current_node1.next

    while current_node2:
        current_node2.data['number'] -= 1
        current_node2 = current_node2.next


def main():
    animal_home = AnimalShelter()
    animal_home.enqueue('dog', 'two')
    animal_home.enqueue('cat', 'eleven')
    animal_home.enqueue('dog', 'eight')
    animal_home.enqueue('cat', 'five')
    animal_home.enqueue('cat', 'three')
    animal_home.enqueue('cat', 'thirteen')
    animal_home.enqueue('cat', 'nine')
    animal_home.enqueue('dog', 'six')
    animal_home.enqueue('cat', 'seven')
    animal_home.enqueue('dog', 'fourteen')
    animal_home.enqueue('dog', 'four')
    animal_home.enqueue('dog', 'ten')
    animal_home.enqueue('dog', 'twelve')
    animal_home.enqueue('cat', 'one')
    print(animal_home)
    # print(animal_home.dequeue_any())
    # print(animal_home.dequeue_dog())
    print(animal_home)


if __name__ == "__main__":
    main()
