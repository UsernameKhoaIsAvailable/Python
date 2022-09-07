from linked_list import LinkedList
class LinkedList24(LinkedList):
    def partition(self, x):
        current_node = self.head.next
        prev_node = self.head
        while current_node != None:
            if current_node.data < x:
                prev_node.next = current_node.next
                current_node.next = self.head
                self.head = current_node
                current_node = prev_node.next
                   
            else:
                prev_node.next = current_node
                prev_node = current_node
                current_node = current_node.next
           
ex = LinkedList24()
ex.add(9)
ex.add(1)
ex.add(8)
ex.add(2)
ex.add(3)
ex.add(6)
ex.add(4)
ex.add(5)
ex.add(7)
ex.add(10)
print(ex)
ex.partition(6)
print(ex)
