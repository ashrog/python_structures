class Stack:
    def  __init__(self):
        self.__elements = []

    def isEmpty(self):
        return len(self.__elements) == 0
    def peek(self):
        return self.__elements[-1]

    def push(self, data):
        self.__elements.append(data)

    def pop(self):
        if len(self.__elements) != 0:
           return self.__elements.pop()
        else:
            return None
    def getSize(self):
         return len(self.__elements)

def main():
    myStack = Stack()
    myStack.push(10)
    myStack.push(39)
    myStack.push(43)

    while myStack.getSize() > 0:
        print(myStack.pop(), end = " ")
    # print()


# main()
