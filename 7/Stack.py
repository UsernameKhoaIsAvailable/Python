from linked_list import LinkedList

class EmptyStackException(Exception):
    pass

class Stack:

    def __init__(self):
        self.data_list = LinkedList()

    def empty(self):
        return self.data_list.head is None

    def peek(self):
        return self.data_list.head.data

    def pop(self):
        if self.data_list.head is None:
            raise EmptyStackException

        return_node = self.head
        self.head = self.head.next
        self.length -= 1
        return return_node.data
    
    def push(self, data):
        self.data_list.add_first(data)

    def search(self, data):
        current_node = self.data_list.head
        index = self.data_list.length - 1

        while current_node != None:
            if current_node.data == data:
                return index

            current_node = current_node.next
            index -= 1

        return -1

    def size(self):
        return self.data_list.length

    def __str__(self):
        current_node = self.data_list.head
        return_str = ''

        while current_node != None:
            return_str += str(current_node.data)
            current_node = current_node.next

            if current_node != None:
                return_str += ' ,'

        return return_str[::-1]    






# list = Stack()
# # list.pop()
# list.push(1)
# list.push(2)
# list.push(3)
# list.push(4)
# list.push(5)
# list.push(6)
# list.push(7)
# list.push(8)
# print(list)
# print(list.pop())
# print(list)
# print(list.search(5))




