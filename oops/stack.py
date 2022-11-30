from collections import deque
# stack = deque()
# print(dir(stack))

# stack.append("hello")
# stack.append("there")
# stack.append("how")
# stack.append("are")
# stack.append("you")
# print(stack)


class Stack:
    def __init(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self, val):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)