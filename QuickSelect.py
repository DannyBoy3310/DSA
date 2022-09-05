class Quickselect:
    def __init__(self,nums):
        self.nums = nums
        self.start = 0
        self.end = len(nums) - 1
    def run(self,k):
        return self.select(self.start,self.end,k-1)
    def partition(self,start,end):
        pivot_idx = start
        self.swap(pivot_idx,end)
        for i in range(start,end):
            if self.nums[i] < self.nums[end]:
                self.swap(i,start)
                start+=1
        self.swap(start,end)
        return start
    def swap(self,a,b):
        if a!=b:
            self.nums[a],self.nums[b] = self.nums[b],self.nums[a]
    def select(self,start,end,k):
        if start< end:
            pi = self.partition(start,end)
            if pi > k:
                return self.select(start, pi - 1,k)
            elif pi < k:
                return self.select(pi+1,end,k)
            else:
                return self.nums[pi]


nums = [75,32,88,9]
qs = Quickselect(nums)
print(qs.run(1))
