from stack import Stack
OriginStack = Stack()
TempStack = Stack()
class MyQueue():
    def __init__(self):
        self.head_data = None

    def add(self, data):
        OriginStack.push(data)

        if OriginStack.length == 1:
            self.head_data = OriginStack.peek()
        
    def __str__(self):
        current_node = OriginStack.head
        return_str = ''

        while current_node != None:
            return_str += str(current_node.data)
            current_node = current_node.next

            if current_node != None:
                return_str += ' ,'

        return return_str[::-1]

    def peek(self):
        # return_node_data = None

        # while OriginStack.empty() is False:
        #     current_node_data = OriginStack.pop()
        #     TempStack.push(current_node_data)

        # return_node_data = current_node_data

        # while TempStack.empty() is False:
        #         current_node_data = TempStack.pop()
        #         OriginStack.push(current_node_data)
        
        # return return_node_data
        return self.head_data
        
    def poll(self):
        return_node_data = self.head_data

        while OriginStack.empty() is False:
            current_node_data = OriginStack.pop()
            TempStack.push(current_node_data)
        
        TempStack.pop()
        self.head_data = TempStack.head.data

        while TempStack.empty() is False:
                current_node_data = TempStack.pop()
                OriginStack.push(current_node_data)

        return return_node_data

    def empty(self):
        return OriginStack.empty()
    
    def size(self):
        return OriginStack.size()
        


def main():
    queue = MyQueue()
    # print(queue.empty())
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    queue.add(6)
    queue.add(7)
    queue.add(8)
    print(queue)
    print(queue.size())
    print(queue.poll())
    print(queue.size())
    # print(queue)
    # print(queue.head_data)
    # print(queue.empty())
    

if __name__ == "__main__":
    main()