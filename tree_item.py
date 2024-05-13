
class TreeItem:
    parent = None
    def __init__(self, name='', parent=None):
        self.name = name
        self.children = []
        if parent:
            parent.appendChild(self)

    def appendChild(self, item):
        self.insertChild(len(self.children), item)

    def insertChild(self, index, item):
        self.children.insert(index, item)
        item.parent = self

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return -1