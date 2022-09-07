from linked_list import LinkedList
def palindrome(LinkedList):
    current_node =LinkedList.head
    palindrome_str = ''
    while current_node != None:
        palindrome_str += str(current_node.data)
        current_node = current_node.next
    
    if palindrome_str == palindrome_str[::-1]:
        return True
    else:
        return False

ex = LinkedList()
ex.add(2)
ex.add(4)
ex.add(1)
ex.add(6)
ex.add(5)
ex.add(3)
print(palindrome(ex))