from linked_list import LinkedList
def palindrome(_list):
    current_node =_list.head
    list2 = LinkedList()

    while current_node != None:
        list2.add_first(current_node.data)
        current_node = current_node.next
    
    current_node1 = _list.head
    current_node2 = list2.head

    while current_node1 != None:
        if current_node1.data != current_node2.data:
            return False

        current_node1 = current_node1.next
        current_node2 = current_node2.next

    return True
    
    

ex = LinkedList()
ex.add(1)
ex.add(2)
ex.add(3)
ex.add(4)
ex.add(2)
ex.add(1)
print(palindrome(ex))