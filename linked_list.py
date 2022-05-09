class LinkedListIterator:
    def __init__(self, head):
        self.Current = head

    def __next__(self):
        if self.Current == None:
            raise StopIteration
        data = self.Current.Data
        self.Current = self.Current.Next
        return data


class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __iter__(self):
        return LinkedListIterator(self.__head)

    def GetSize(self):
        return self.__size

    def GetElements(self):
        curr = self.__head
        while (curr != None):
            print(curr.Data)
            curr = curr.Next

    def AddFirst(self, data):
        newNode = Node(data)
        if (self.__size == 0):
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            newNode.Next = self.__head
            self.__head = newNode
            self.__size += 1
    def AddLast(self, data):
        newNode = Node(data)
        if (self.__size == 0):
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.Next = newNode
            self.__tail = newNode
            self.__size += 1

    def RemoveFirst(self):
        data = self.__head.Data
        self.__head = self.__head.Next
        self.__size -= 1
        return data

    def RemoveLast(self):
        if (self.__size > 1):
            # if (self.__head.Next == None):
            #     self.__head = None
            # else:
            current = self.__head
            while(current.Next.Next != None):
                current = current.Next

            self.__tail = current
            current.Next = None
            self.__size -= 1

        elif (self.__size == 1):
            self.__head = None
            self.__tail = None
            self.__size -= 1

    def Insert(self,index,data):
        i = 1
        curr = self.__head
        while(i < index):
            curr = curr.Next
            i += 1

        newNode = Node(data)
        newNode.Next = curr.Next
        curr.Next = newNode

    def Remove(self, index):
        i = 1
        curr = self.__head
        while (i < index):
            curr = curr.Next
            i += 1

        curr.Next = curr.Next.Next

    def IsEmpty(self):
        return (self.__size == 0)

    def GetFirst(self):
        if not self.IsEmpty():
            return self.__head
        else:
            print("is empty")

    def GetLast(self):
        if not self.IsEmpty():
            return self.__tail
        else:
            print("is empty")


def main():
    myList = LinkedList()
    myList.AddFirst(4)
    myList.AddFirst(5)
    myList.AddFirst(10)
    # myList.GetElements()
    myList.Insert(2,15)
    # myList.GetElements()
    myList.Insert(2,8)
    myList.GetElements()
    myList.Remove(4)
    # myList.GetElements()

    for data in myList:
        print(data, end=" ")


    # print(myList.GetLast().Data)

# main()