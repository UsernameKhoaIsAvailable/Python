from re import T
from circular_linked_list import CircularLinkedList
def detect_loop(list):
    return list.tail.next.data

list = CircularLinkedList()
list.add('qwerertyuio')
list.add('hello')
list.add('xinchao')
list.add('tambiet')
list.add('vinhbiet')
list.add('hfdjhfjshhf')
list.add('hfujhsfuhsfudhsfjdshf')
list.add('hfueeifonvfnvfueiewnf0')
index = 3
i = 0
current_node = list.head

while current_node != None:
    if i == index:
        list.tail.next = current_node
        break

    current_node = current_node.next
    i += 1

print(detect_loop(list))