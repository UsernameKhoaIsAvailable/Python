from linked_list import LinkedList


class EmptyStackException(Exception):
    pass


class Stack:

    def __init__(self):
        self.data_list = LinkedList()

    def empty(self): #O(1)
        return self.data_list.head is None

    def peek(self): #O(1)
        return self.data_list.head.data

    def pop(self): #O(1)
        if self.data_list.head is None:
            raise EmptyStackException

        return_node = self.data_list.head
        self.data_list.head = self.data_list.head.next
        self.data_list.length -= 1
        return return_node.data
    
    def push(self, data): #O(1)
        self.data_list.add_first(data)

    def search(self, data): #O(n)
        current_node = self.data_list.head
        index = self.data_list.length - 1

        while current_node:
            if current_node.data == data:
                return index

            current_node = current_node.next
            index -= 1

        return -1

    def size(self): #O(1)
        return self.data_list.length

    def __str__(self):
        current_node = self.data_list.head
        _list = []

        while current_node:
            _list.append(str(current_node.data))
            current_node = current_node.next

        return ", ".join(_list[::-1])


def main():
    _list = Stack()
    # _list.pop()
    _list.push(1)
    _list.push(2)
    _list.push(3)
    _list.push(4)
    _list.push(5)
    _list.push(6)
    _list.push(7)
    _list.push(8)
    print(_list)
    print(_list.pop())
    print(_list)
    # print(_list.search(5))


if __name__ == "__main__":
    main()


