from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.data_list = LinkedList()

    def add(self, data): #O(1)
        self.data_list.add(data)

    def peek(self): #O(1)
        return self.data_list.head.data

    def poll(self): #O(1)
        return_node = self.data_list.head
        self.data_list.remove_at(0)
        return return_node.data

    def empty(self): #O(1)
        return self.data_list.head is None

    def size(self): #O(1)
        return self.data_list.length

    def __str__(self):
        return self.data_list.__str__()


def main():
    _list = Queue()
    _list.add(1)
    _list.add(2)
    _list.add(3)
    _list.add(4)
    _list.add(5)
    _list.add(6)
    _list.add(7)
    _list.add(8)
    print(_list)
    print(_list.size())
    print(_list.peek())
    print(_list.poll())
    print(_list)
    print(_list.size())


if __name__ == "__main__":
    main()
