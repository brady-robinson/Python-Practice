class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

bst = BinarySearchTree(15)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
# bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)
# bst.insert_node(21)

print(bst.find_node(8))
print(bst.find_node(12))
print(bst.find_node(20))
print(bst.find_node(17))
print(bst.find_node(25))
print(bst.find_node(19))

print(bst.find_node(14))
# print(bst.find_node(3))
# print(bst.find_node(0))
# print(bst.find_node(16))
# print(bst.find_node(7))
# print(bst.find_node(50))