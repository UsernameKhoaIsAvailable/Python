from doubly_linked_list import DoublyLinkedList

def plus_2_linked_list(list1, list2):
    num1 = convert_linked_list_to_number(list1)
    num2 = convert_linked_list_to_number(list2)
    result = num1 + num2
    return result

def convert_linked_list_to_number(llist):
    i = pow(10, llist.length - 1)
    result = 0
    current_node = llist.tail
    while current_node != None:
        result += current_node.data * i
        current_node = current_node.prev
        i /= 10

    return result

def sum_lists(list1, list2):
    sum = plus_2_linked_list(list1, list2)
    SumList = DoublyLinkedList()
    
    while sum != 0:
        num = int(sum % 10)
        SumList.add(num)
        sum = int(sum / 10)

    return SumList


num1 = DoublyLinkedList()
num1.add(7)
num1.add(1)
num1.add(6)

num2 = DoublyLinkedList()
num2.add(5)
num2.add(9)
num2.add(2)

SumList = sum_lists(num1, num2)
print(SumList)
# print(convert_LinkedList_to_number(num2))