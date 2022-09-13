from Stack import Stack
class Stack32(Stack):
    def push(self, data):
        super().push(data)

        if self.length == 1:
            self.min = self.head.data
        else:
            if self.head.data < self.min:
                self.min = self.head.data
         

    def __init__(self):
        super().__init__()
        self.min = 0

    def Minimum(self):
        return self.min

def main():
    _list = Stack32()
    _list.push(2)
    _list.push(3)
    _list.push(4)
    _list.push(5)
    _list.push(6)
    _list.push(7)
    _list.push(8)
    _list.push(1)
    print(_list)
    print(_list.Minimum())

if __name__ == '__main__':
    main()