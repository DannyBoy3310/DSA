class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    """
        FOR HASHTABLE USING CHAINING
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for idx,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                self.arr[h][idx] = (key,value)
                return
        self.arr[h].append((key,value))
        return
    def __getitem__(self, key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                del self.arr[h][idx]"""

    #FOR HASHTABLE USING LINEAR PROBING
    def find_slots(self,key,h):
        slots = self.prob_range(key)
        for slot in slots:
            if self.arr[slot] is None:
                return slot
            if self.arr[slot][0]==key:
                return slot
        raise Exception("Hashmap Full")

    def prob_range(self,key):
        h = self.get_hash(key)
        return [*range(h,self.MAX)]+[*range(0,h)]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,value)
        else:
            slot = self.find_slots(key,h)
            self.arr[slot] = (key,value)
        print(self.arr)

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        ranges = self.prob_range(key)
        for slot in ranges:
            ele = self.arr[slot]
            if ele is None:
                return
            if ele[0]==key:
                return ele[1]




if __name__ == "__main__":
    ht = Hashtable()
    ht["march 10"] = "Daniel"
    ht["march 17"] = "Rajakumar"
    ht["march 6"] = "Anitha"
    ht["january 20"] = "Sherlyn"
    print(ht["march 10"])