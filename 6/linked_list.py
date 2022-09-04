class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    def add(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_at(self, index, new_data):
        if self.length < index:
            raise Exception(f"Cannot insert at index {index}")

        new_node = Node(new_data)
        self.length += 1   

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        prev_node = None
        i = 0

        while current_node != None:
            if i == index:
                new_node.next = current_node
                prev_node.next = new_node
                break
            else:
                prev_node = current_node
                current_node = current_node.next
                i += 1
        
    def __str__(self):
        current_node = self.head
        return_str = ''
        while current_node != None:
            return_str += current_node.data
            current_node = current_node.next
            if current_node != None:
                return_str += ', '
        return return_str    

    def add_first(self, data):
        self.add_at(0, data)

    def contains(self, data):
        current_node = self.head
        while current_node != None:
            if data == current_node.data:
                return True
            current_node = current_node.next

        return False

    def get(self, index):
        if self.length < index:
            raise Exception(f"Cannot get data at index {index}")

        current_node = self.head
        i = 0
        while current_node != None:
            if i == index:
                return current_node.data
            i += 1
            current_node = current_node.next

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self.length - 1)

# ex = LinkedList()
# ex.add('hfdjhfjshhf')
# ex.add('hfujhsfuhsfudhsfjdshf')
# ex.add('hfueeif onvfnvfueiewnf0')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add_at(4, 'fejhfddkndvdmxxcncnxzmcnz')
# ex.add_first('poopjdknvdnvkseiasdjask')

# # print(ex.contains('hfdjhfjshhfdfdfd'))
# print(ex.get(6))
# # print(ex.get_first())
# # print(ex.get_last())
# print(ex)

        
    

    