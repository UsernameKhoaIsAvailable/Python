from linked_list import LinkedList
class LinkedList23(LinkedList):
    def del_mid_node(self):
        index = int(self.length / 2)
        
        current_node = self.head
        prev_node = None
        i = 0

        while current_node != None:
            if i == index:
                prev_node.next = current_node.next
                self.length -= 1
                return
            prev_node = current_node
            current_node = current_node.next
            i += 1

# ex = LinkedList23()
# ex.add('hello')
# ex.add('hello')
# ex.add('xinchao')
# ex.add('tambiet')
# ex.add('vinhbiet')
# ex.add('hfdjhfjshhf')
# ex.add('hfujhsfuhsfudhsfjdshf')
# ex.add('hfueeif onvfnvfueiewnf0')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# print(ex)
# print(ex.length)
# ex.del_mid_node()
# print(ex)
# print(ex.length)

