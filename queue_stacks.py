#creating a queue given two stacks to hold and get back from the other
from stackk import Stack

class Queue:
    def __init__(self):
        self.__elements = Stack()
        self.__place = Stack()

    def isEmpty(self):
        return self.__elements.isEmpty()


    def getSize(self):
        return self.__elements.getSize()

    def EnQueue(self, data):
        return self.__elements.push(data)

    def DeQueue(self):
        if self.__place.isEmpty():
            while (not self.__elements.isEmpty()):
                self.__place.push(self.__elements.pop())
                return self.__place.pop()

def main():
    myQueue = Queue()
    myQueue.EnQueue(10)
    myQueue.EnQueue(20)
    myQueue.DeQueue()
    myQueue.EnQueue(30)

    while (myQueue.getSize() > 0):
        print(myQueue.DeQueue(), end = " ")
    print()
main()