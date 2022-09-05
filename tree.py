class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def printtree(self):
        spaces = " " * self.get_level() * 5
        prefix = spaces + "|-->" if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            child.printtree()
    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level+=1
        return level



def build_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Surface Book"))
    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Iphone"))
    mobile.add_child(TreeNode("Nokia"))
    tv = TreeNode("Television")
    tv.add_child(TreeNode("Onida"))
    tv.add_child(TreeNode("Realme"))
    tv.add_child(TreeNode("LG"))
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)
    return root


if __name__=="__main__":
    root = build_tree()
    root.printtree()
