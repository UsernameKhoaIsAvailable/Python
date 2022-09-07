from unittest import result
from Doubly_LinkedList import DoublyLinkedList

def plus_2_LinkedList(LinkedList1, LinkedList2):
    num1 = convert_LinkedList_to_number(LinkedList1)
    num2 = convert_LinkedList_to_number(LinkedList2)
    result = num1 + num2
    return result

def convert_LinkedList_to_number(LinkedList):
    i = pow(10, LinkedList.length - 1)
    result = 0
    current_node = LinkedList.tail
    while current_node != None:
        result += current_node.data * i
        current_node = current_node.prev
        i /= 10

    return result

def sum_lists(LinkedList1, LinkedList2):
    sum = plus_2_LinkedList(LinkedList1, LinkedList2)
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