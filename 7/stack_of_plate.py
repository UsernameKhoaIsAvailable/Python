from stack import Stack


class SetOfStack:
    def __init__(self, max_length: int):
        self.max_length: int = max_length
        self.stacks: list[Stack] = []

    def push(self, data):
        if len(self.stacks) == 0 or self.stacks[-1].size() == self.max_length:
            new_stack = Stack()
            self.stacks.append(new_stack)
            new_stack.push(data)
        else:
            self.stacks[-1].push(data)

    def pop(self):
        try:
            if self.stacks[-1].size() != 1:
                return self.stacks[-1].pop()
        except IndexError:
            pass

        return_data = self.stacks[-1].pop()
        self.stacks.pop()
        return return_data

    def pop_at(self, index):
        if index >= len(self.stacks):
            raise IndexError("invalid stack index")
        if index == len(self.stacks) - 1:
            return self.pop()

        return_data = self.stacks[index].pop()
        temp_stack = Stack()
        i = len(self.stacks) - 1
        prev_num_of_stack = len(self.stacks)

        while i > index:
            current_node_data = self.pop()
            temp_stack.push(current_node_data)

            if len(self.stacks) < prev_num_of_stack:
                i -= 1
                prev_num_of_stack = len(self.stacks)

        while temp_stack.empty() is False:
            current_node_data = temp_stack.pop()
            self.push(current_node_data)

        return return_data

    def __str__(self):
        return_str = ''

        for i in range(len(self.stacks)):
            return_str += self.stacks[i].__str__()

            if i < len(self.stacks) - 1:
                return_str += ', '

        return return_str


def main():
    _list = SetOfStack(5)
    _list.push(1)
    _list.push(2)
    _list.push(3)
    _list.push(4)
    _list.push(5)
    _list.push(6)
    _list.push(7)
    _list.push(8)
    _list.push(9)
    _list.push(10)
    _list.push(11)
    _list.push(12)
    _list.push(13)
    _list.push(14)
    _list.push(15)
    _list.push(16)
    print(_list)
    print(_list.pop_at(1))
    print(_list)
    print(_list.stacks[2])
    # print(_list.stacks[1].size())


if __name__ == "__main__":
    main()
