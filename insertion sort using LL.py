class Listnode:
    def __init__(self,val=None,next = None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy = Listnode(0)
        dummy.next = nodetoinsert = head
        while head and head.next:
            if head.val > head.next.val:
                nodetoinsert = head.next
                nodetoinsertpre = dummy
                while nodetoinsertpre.next.val < nodetoinsert.val:
                    nodetoinsertpre = nodetoinsert
                head.next = nodetoinsert.next
                nodetoinsert.next = nodetoinsertpre.next
                nodetoinsert.next = nodetoinsert
            else:
                head = head.next
        return dummy.next

dummy = head = Listnode(4)
head.next = Listnode(3)
head = head.next
head.next = Listnode(1)
head = head.next
head.next = Listnode(2)
head = head.next
s = Solution()
ans = s.insertionSortList(dummy)
while ans:
    print(ans.val,end="-->")
