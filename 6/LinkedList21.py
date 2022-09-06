from linked_list import LinkedList

class LinkedList21(LinkedList):
    def remove_dups(self):
        current_node = self.head
        while current_node != None:
            prev_dup_node = current_node
            dup_node = prev_dup_node.next
            while dup_node != None:
                if current_node.data == dup_node.data:
                    prev_dup_node.next = dup_node.next
                    self.length -= 1

                    if prev_dup_node.next == None:
                        self.tail = prev_dup_node
                    return
                else:
                    prev_dup_node = dup_node
                    dup_node = dup_node.next
            current_node = current_node.next
    


# ex =LinkedList21()
# ex.add('hello')
# ex.add('hello')
# ex.add('xinchao')
# ex.add('tambiet')
# ex.add('vinhbiet')
# print(ex)
# ex.remove_dups()
# print(ex)
# print(ex.length)
# print(ex.head.data)
# print(ex.tail.data)

