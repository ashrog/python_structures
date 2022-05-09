#creating a queue using the linked list used here
from linked_list import LinkedList
class Queue:
    def __init__(self):
        self.__elements = LinkedList()
    def isEmpty(self):
        return self.__elements.IsEmpty()
    def getSize(self):
        return self.__elements.GetSize()

    def EnQueue(self, data):
        return self.__elements.AddLast(data)

    def DeQueue(self):
        return self.__elements.RemoveFirst()

def main():
    myQueue = Queue()
    myQueue.EnQueue(10)
    myQueue.EnQueue(20)
    myQueue.EnQueue(30)

    while (myQueue.getSize() > 0):
        print(myQueue.DeQueue(), end = " ")
    print()
main()