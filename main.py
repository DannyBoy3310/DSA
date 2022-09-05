"""Program for Singly Linked List"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        liststr = ""
        itr = self.head
        while itr:
            liststr += str(itr.data) + "-->"
            itr = itr.next
        print(liststr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):  # inserting values after the end
        for el in data_list:
            self.insert_at_end(el)

    def count_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def insert_at(self,position,data):
        if position<0 or position > self.count_length():
            raise IndexError("Index out of Range")
        if position==0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        i = 0
        while(i != position -1):
            itr = itr.next
            i+=1
        node = Node(data,itr.next)
        itr.next = node
    def insert_after_value(self,data_after,data):
        if self.head.data == data_after:
            node = Node(data,self.head.next)
            self.head.next = node
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data,itr.next)
                return
            else:
                itr = itr.next
        print("Element not in List")





    def remove_at(self, position):
        if position < 0 or position > self.count_length():
            raise IndexError("Invalid Index")
        if position == 0:
            self.head = self.head.next
            return
        i = 0
        itr = self.head
        while (i != position - 1):
            itr = itr.next
            i += 1
        itr.next = itr.next.next
        return
    def remove_by_value(self,data):
        itr = self.head
        if self.head.data == data:
            itr = self.head
            self.head = self.head.next
            itr.next = None
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            else:
                itr = itr.next
        print("Element not in List")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(46)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(25)
    ll.insert_at_end(96)
    ll.insert_values([6, 7, 9, 1, 23])
    print(ll.count_length())
    ll.printlist()
    ll.remove_at(2)
    #ll.remove_at(10)
    ll.printlist()
    ll.insert_at(3,77)
    ll.remove_by_value(7)
    ll.remove_by_value(16)
    ll.insert_after_value(77,36)
    ll.printlist()