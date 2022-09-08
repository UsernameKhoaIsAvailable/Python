class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = self.head
        self.length += 1

    def __str__(self):
        current_node = self.head
        return_str = ''
        i = 0

        while i != self.length:
            return_str += str(current_node.data)
            current_node = current_node.next

            if i != self.length - 1:
                return_str += ', '
            
            i += 1

        return return_str

# ex = CircularLinkedList()
# ex.add('qwerertyuio')
# ex.add('hello')
# ex.add('hello')
# ex.add('xinchao')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('tambiet')
# ex.add('vinhbiet')
# ex.add('hfdjhfjshhf')
# ex.add('hfujhsfuhsfudhsfjdshf')
# ex.add('hfueeifonvfnvfueiewnf0')
# print(ex)