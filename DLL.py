"""Program for Doubly Linked List"""
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        if self.head is None:
            node = Node(data,None,self.head)
            self.head = node
            return
        node = Node(data,None,self.head)
        self.head.prev = node
        self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,itr,None)
        return
    def remove_at(self,index):
        if index<0 or index> self.length():
            raise Exception("Index out of range")
        if index==0:
            itr = self.head
            self.head = self.head.next
            self.prev = None
            return
        i = 0
        itr = self.head
        while(i < index):
            itr = itr.next
            i+=1
        itr.prev.next = itr.next
        if itr.next:
            itr.next.prev = itr.prev
        return


    def length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def printlist(self):
        liststr=" "
        itr = self.head
        while itr:
            liststr += str(itr.data)+"<-->"
            itr=itr.next
        print(liststr)

if __name__=="__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(46)
    dll.insert_at_end(102)
    dll.insert_at_beginning(25)
    dll.insert_at_beginning(77)
    dll.insert_at_beginning(64)
    dll.printlist()
    dll.remove_at(1)
    dll.printlist()

