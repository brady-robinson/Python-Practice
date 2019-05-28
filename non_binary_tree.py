class Tree(object):
    def __init__(self):
        self.left = None
        self.child = []
        self.data = []
    def create_children(self, amount):
        for i in range(0, amount):
            self.child.append(Tree())
    def set_children_values(self, list):
        for i in range(0, len(list)):
            self.data.append(list[i])

root = Tree()
root.create_children(3)
root.set_children_values([5, 6, 7])
root.child[0].create_children(2)
root.child[0].set_children_values([1, 2])

print(root.data[0])
print(root.child[0].data[0])