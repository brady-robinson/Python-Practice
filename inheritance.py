class Paper:
    def __init__(self, name):
        self.name = name

    def recyclable(self):
        return True


class Bag(Paper):
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

paper_bag = Bag()
paper_bag.recyclable
print(paper_bag.recyclable())

print(isinstance(paper_bag, Bag))
print(issubclass(Bag, Paper))