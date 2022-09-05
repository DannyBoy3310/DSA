class TreeNode:
    def __init__(self,name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def printree(self,param):
        if param=="name":
            spaces = " " * self.get_level() * 5
            prefix = spaces + "|-->" if self.parent else ""
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.printree(param)

        elif param=="designation":
            spaces = " " * self.get_level() * 5
            prefix = spaces + "|-->" if self.parent else ""
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.printree(param)

        elif param=="both":
            spaces = " " * self.get_level() * 5
            prefix = spaces + "|-->" if self.parent else ""
            print("{}{} ({})".format(prefix,self.name,self.designation))
            if self.children:
                for child in self.children:
                    child.printree(param)

    def printtreelevel(self,levels):
        level = self.get_level()
        if level <= levels:
            spaces = " " * self.get_level() * 5
            prefix = spaces + "|-->" if self.parent else ""
            print("{}{}".format(prefix, self.name))
            if self.children:
                for child in self.children:
                    child.printtreelevel(levels)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level+=1
        return level
def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root
if __name__ == '__main__':
    root = build_location_tree()
    root.printtreelevel(1)
    root.printtreelevel(2)
    root.printtreelevel(3)