from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def length(self):
        return len(self.container)
    def find_match(self,ch1,ch2):
        matches = {"}":"{",")":"(","]":"["}
        return matches[ch1]==ch2
    def is_balanced(self,value):
        for ch in value:
            if ch == "(" or ch =="{" or ch =="[":
                self.push(ch)
            elif ch=="}" or ch=="]" or ch==")":
                if self.is_empty():
                    return False
                elif not self.find_match(ch,self.pop()):
                    return False
        return self.length()==0
if __name__=="__main__":
    stack = Stack()
    print(stack.is_balanced("{(a+b)}"))
    print(stack.is_balanced("(a+b)*{a+b*(c//2)}*[5--3]"))
