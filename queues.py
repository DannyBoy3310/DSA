from collections import deque
import time
import threading
class queues:
    def __init__(self):
        self.container = deque()
    def enqueue(self,value):
        self.container.appendleft(value)
    def dequeue(self):
        return self.container.pop()
    def front(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def length(self):
        return len(self.container)
    def front(self):
        return self.container[-1]
q = queues()
def place_orders(order_list):
    for order in order_list:
        time.sleep(0.5)
        print("order places: ",order)
        q.enqueue(order)
def serve_order():
    time.sleep(1)
    while(q.is_empty()==False):
        order = q.dequeue()
        print("order served: ",order)
        time.sleep(2)
def print_binary():
    while(q.is_empty()==False):
        num = q.dequeue()
        print(num)
if __name__=="__main__":
    # t1 = threading.Thread(target=place_orders,args=(['pizza','samosa','pasta','biryani','burger'],))
    # t2 = threading.Thread(target=serve_order)
    # t1.start()
    # t2.start()
    for num in range(1,11):
        q.enqueue(bin(num)[2::])
    print_binary()
