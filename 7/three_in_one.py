array = []
num_of_stack = 0 
class Stack:
    def __init__(self):
        global num_of_stack
        self.top_index = None
        self.length = 0
        num_of_stack += 1
        
    def empty(self):
        return self.top_index is None

    def push(self, data):
        # if num_of_stack == 1:
        #     array.append(data)
        #     self.length += 1
        #     self.top_index = len(array) - 1
        # else:
        if self.length == 0:
            array.append(data)
            self.top_index = len(array) - 1
            self.length += 1
        else:
            try:
                if array[self.top_index + 1] == '':
                    array.pop(self.top_index + 1)
            except:
                pass
            finally: 
                array.insert(self.top_index + 1, data)
                self.length += 1
                self.top_index += 1
        
    def __str__(self):
        if self.length == 0:
            return "Empty"
        elif self.length - self.top_index == 1:
            return str(array[:self.top_index + 1])
        else:
            return str(array[self.top_index - self.length + 1 : self.top_index + 1])

    def peek(self):
        return array[self.top_index]

    def pop(self):
        return_item = array[self.top_index]
        array.pop(self.top_index)
        array.insert(self.top_index,'')
        self.top_index -= 1
        self.length -= 1
        return return_item

def main():
    stack1 = Stack()
    stack2 = Stack()

    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)

    stack2.push(11)
    stack2.push(12)
    stack2.push(13)
    stack2.push(14)

    print(stack1.pop())
    print(stack2.pop())
    stack1.push(32)
    print(stack1)
    print(stack2)
    print(array)

if __name__ == "__main__":
    main()

    