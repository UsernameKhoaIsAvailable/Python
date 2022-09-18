from linked_list import LinkedList
class Queue:
    def __init__(self):
        self.data_list = LinkedList()
    
    def add(self, data):
        self.data_list.add(data)

    def peek(self):
        return self.data_list.head.data

    def poll(self):
        return_node = self.data_list.head
        self.data_list.remove_at(0)
        return return_node.data

    def empty(self):
        return self.data_list.head is None

    def size(self):
        return self.data_list.length
    
    def __str__(self):
        return str(self.data_list.__str__())
        
def main():
    list = Queue()
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    list.add(5)
    list.add(6)
    list.add(7)
    list.add(8)
    # print(list)
    # print(list.size())
    # print(list.peek())
    # print(list.poll())
    # print(list)
    # print(list.size())
    # print(list.size())
    
if __name__ == "__main__":
    main()