from linked_list import LinkedList
class LinkedList22(LinkedList):
    def return_Kth_to_last(self, K):
        if self.length <= K or K < 0:
            raise Exception(f"Cannot return the {K}th to last element")
        index = self.length - K - 1
        current_node = self.head
        i = 0

        while current_node != None:
            if i == index:
                return current_node.data
            current_node = current_node.next
            i += 1
       
# ex = LinkedList22()
# ex.add('hello')
# ex.add('hello')
# ex.add('xinchao')
# ex.add('tambiet')
# ex.add('vinhbiet')
# ex.add('hfdjhfjshhf')
# ex.add('hfujhsfuhsfudhsfjdshf')
# ex.add('hfueeifonvfnvfueiewnf0')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# ex.add('qwerertyuio')
# print(ex)
# print(ex.return_Kth_to_last(56))