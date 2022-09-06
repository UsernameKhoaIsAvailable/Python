from linked_list import LinkedList

class LinkedList2(LinkedList):
    def remove_dups(self):
        current_node = self.head
        while current_node != None:
            prev_dup_node = current_node
            dup_node = prev_dup_node.next
            while dup_node != None:
                if current_node.data == dup_node.data:
                    prev_dup_node.next = dup_node.next
                    return
                else:
                    prev_dup_node = dup_node
                    dup_node = dup_node.next
            current_node = current_node.next


ex =LinkedList2()
ex.add('xinchao')
ex.add('hello')
ex.add('tambiet')
ex.add('vinhbiet')
ex.add('hello')
print(ex)
ex.remove_dups()
print(ex)

