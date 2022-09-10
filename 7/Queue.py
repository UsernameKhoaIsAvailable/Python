from linked_list import LinkedList
class Queue(LinkedList):
    def peek(self):
        return self.head.data

    def poll(self):
        return_node = self.head
        self.remove_at(0)
        return return_node.data

    def empty(self):
        return self.head is None

    def size(self):
        return self.length

# list = Queue()
# list.add(1)
# list.add(2)
# list.add(3)
# list.add(4)
# list.add(5)
# list.add(6)
# list.add(7)
# list.add(8)
# # print(list)
# # print(list.length)
# # print(list.peek())
# # print(list.poll())
# # print(list)
# # print(list.length)
# print(list.size())