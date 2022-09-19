from stack import Stack


class Stack32(Stack):
    def push(self, data):
        super().push(data)
        self.sorted_list.append(data)
        self.sorted_list.sort(reverse=True)

    def __init__(self):
        super().__init__()
        self.sorted_list = []

    def minimum(self):
        return self.sorted_list[-1]

    def pop(self):
        self.sorted_list.remove(self.data_list.head.data)
        return super().pop()


def main():
    _list = Stack32()
    _list.push(2)
    _list.push(3)
    _list.push(6)
    _list.push(7)
    _list.push(4)
    _list.push(5)
    _list.push(1)
    _list.push(8)
    print(_list)
    print(_list.minimum())
    print(_list.pop())
    print(_list.minimum())


if __name__ == '__main__':
    main()
