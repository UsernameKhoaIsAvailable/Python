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
        if self.length <= index:
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
                return
            
            prev_node = current_node
            current_node = current_node.next
            i += 1
        
    def __str__(self):
        current_node = self.head
        return_str = ''

        while current_node != None:
            return_str += str(current_node.data)
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
        if self.length <= index:
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

    def index_of(self, data):
        current_node = self.head
        i = 0

        while current_node != None:
            if current_node.data == data:
                return i
            
            current_node = current_node.next
            i += 1

        return -1
    
    def last_index_of(self, data):
        current_node = self.head
        i = 0
        last_i = 0

        while current_node != None:
            if current_node.data == data:
                last_i = i

            current_node = current_node.next
            i += 1

        current_node = self.head

        while current_node != None:
            if current_node.data == data:
                return last_i

            current_node = current_node.next

        return -1       
        
    def remove_at(self, index):
        if self.length <= index:
            raise Exception(f"Cannot remove data at index {index}")

        self.length -= 1

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        prev_node = None
        i = 0

        while current_node != None:
            if i == self.length:   
                self.tail = prev_node
                prev_node.next = None
                return
            if i == index:
                prev_node.next = current_node.next
                return
            
            prev_node = current_node
            current_node = current_node.next
            i += 1
            
    def remove(self, data):
        if self.head.data == data:
            self.remove_at(0)
            return
        
        current_node = self.head
        prev_node = None

        while current_node != None:
            if current_node == self.tail:
                self.remove_at(self.length - 1)
                return
            if current_node.data == data:
                prev_node.next = current_node.next
                self.length -= 1
                return

            prev_node = current_node
            current_node = current_node.next

    def remove_last(self):
        node = self.tail
        self.remove_at(self.length - 1)
        return node.data

    def set(self, index, data):
        if self.length <= index:
            raise Exception(f"Cannot replace data at index {index}")
        if index == 0:
            self.head.data = data
            return

        current_node = self.head
        i = 0
        prev_node = None

        while current_node != None:
            if i == index:
                current_node.data = data
                prev_node.next = current_node
                return
            
            prev_node = current_node
            current_node = current_node.next
            i += 1

    def size(self):
        return self.length

ex = LinkedList()
ex.add('qwerertyuio')
ex.add('hello')
ex.add('hello')
ex.add('xinchao')
ex.add('qwerertyuio')
ex.add('qwerertyuio')
ex.add('tambiet')
ex.add('vinhbiet')
ex.add('hfdjhfjshhf')
ex.add('hfujhsfuhsfudhsfjdshf')
ex.add('hfueeifonvfnvfueiewnf0')
# ex.add_at(4, 'fejhfddkndvdmxxcncnxzmcnz')
# ex.add_first('poopjdknvdnvkseiasdjask')
# print(ex.contains('hfdjhfjshhfdfdfd'))
# print(ex.get(6))
# print(ex.get_first())
# print(ex.get_last())
# print(ex)
# ex.set(6, 'halo')
# print(ex)
# print(ex.head.data)
# print(ex.tail.data)
# print(ex.size())




        
    

    