from linked_list import LinkedList
class LinkedList23(LinkedList):
    def del_mid_node(self, data):
        current_node = self.head.next
        prev_node = self.head
        
        while current_node != self.tail:
            if current_node.data == data:
                prev_node.next = current_node.next
                self.length -= 1
            if prev_node.next.data != data:
                prev_node = current_node

            current_node = current_node.next
        
ex = LinkedList23()
ex.add('qwerertyuio')
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
print(ex)
print(ex.length)
ex.del_mid_node('qwerertyuio')
print(ex)
print(ex.length)

