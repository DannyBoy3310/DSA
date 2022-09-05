class BSTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if self.data==data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left  = BSTnode(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTnode(data)

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements
    def preorder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.preorder()
        if self.right:
            elements+=self.right.preorder()
        return elements
    def postorder(self):
        elements =[]
        if self.left:
            elements+=self.left.preorder()
        if self.right:
            elements+=self.right.preorder()
        elements.append(self.data)
        return elements

    def search(self,val):
        if val==self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum+=self.left.calculate_sum()
        if self.right:
            sum+=self.right.calculate_sum()
        return sum
    def find_min(self):
        if not self.left:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()

    def delete_node(self,data):
        if data < self.data:
            if self.left:
               self.left =  self.left.delete_node(data)
        elif data> self.data:
            if self.right:
               self.right =  self.right.delete_node(data)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            mini = self.right.find_min()
            self.data = mini
            self.right = self.right.delete_node(mini)
        return self

    def delete_node_using_left(self,data):
        if data < self.data:
            if self.left:
               self.left =  self.left.delete_node_using_left(data)
        elif data> self.data:
            if self.right:
               self.right =  self.right.delete_node_using_left(data)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            maxi = self.left.find_max()
            self.data = maxi
            self.left = self.left.delete_node_using_left(maxi)
        return self
    def find_leaf_nodes(self,leafs=[]):
        if self.left is None and self.right is None:
            leafs.append(self.data)
            return leafs
        if self.left:
            self.left.find_leaf_nodes(leafs)
        if self.right:
            self.right.find_leaf_nodes(leafs)
        return leafs

def bfs(root):
    if root is None:
        return
    queue = [root]
    while (len(queue) > 0):
        print(queue[0].data,end=" ")
        ele = queue.pop(0)
        if ele.left:
            queue.append(ele.left)
            
        if ele.right:
            queue.append(ele.right)





def build_bst(elements):
    root = BSTnode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__=="__main__":
    elements = [17,4,15,20,9,23,18,34,97]
    roots = build_bst(elements)
    print(roots.inorder())
    print(roots.search(4))
    print(roots.calculate_sum())
    print(roots.find_min())
    print(roots.find_max())
    roots.delete_node_using_left(23)
    print(roots.inorder())
    print(roots.find_leaf_nodes())