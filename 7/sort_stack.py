from stack import Stack


def sort_stack(origin_stack: Stack):
    origin_stack_size = origin_stack.size()
    temp_element = origin_stack.pop()
    temp_stack = Stack()
    temp_stack.push(temp_element)
    temp_element = origin_stack.pop()

    while temp_stack.size() != origin_stack_size:
        if temp_stack.empty() is True or temp_element > temp_stack.peek():
            temp_stack.push(temp_element)

            if origin_stack.empty() is False:
                temp_element = origin_stack.pop()

            continue

        temp_element2 = temp_stack.pop()
        origin_stack.push(temp_element2)

    while temp_stack.empty() is False:
        temp_element = temp_stack.pop()
        origin_stack.push(temp_element)

    return origin_stack


def main():
    _list = Stack()
    _list.push(7)
    _list.push(11)
    _list.push(2)
    _list.push(9)
    _list.push(3)
    _list.push(6)
    _list.push(5)
    _list.push(4)
    _list.push(12)
    _list.push(8)
    _list.push(10)
    _list.push(1)
    print(_list)
    sort_stack(_list)
    print(_list)


if __name__ == '__main__':
    main()
