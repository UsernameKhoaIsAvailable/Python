from linked_list import LinkedList
def intersect(list1, list2):
    current_node_list1 = list1.head
    while current_node_list1 != None:
        current_node_list2 = list2.head

        while current_node_list2 != None:
            if current_node_list1.next == current_node_list2.next:
                return return_intersection(current_node_list1.next)
            
            current_node_list2 = current_node_list2.next

        current_node_list1 = current_node_list1.next

def return_intersection(node):
    current_node = node
    return_str = ''
    while current_node != None:
        return_str += str(current_node.data)
        return_str += ', '
        current_node = current_node.next
    
    return return_str

list1 = LinkedList()
list1.add('qwerertyuio')
list1.add('hello')
list1.add('xinchao')
list1.add('tambiet')
list1.add('vinhbiet')
list1.add('hfdjhfjshhf')
list1.add('hfujhsfuhsfudhsfjdshf')
list1.add('hfueeifonvfnvfueiewnf0')

list2 = LinkedList()
list2.add('4634736743674')
list2.add('54545455')
list2.add('784245361313')
current_node = list1.head
i = 0
index = 3

while current_node != None:
    if i == index:
        list2.tail.next = current_node
        list2.tail = list1.tail
        list2.length += 5
        break

    current_node = current_node.next
    i += 1

print(list1)
print()
print(list2)
print()
print(intersect(list1, list2))

        
