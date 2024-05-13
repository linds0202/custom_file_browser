from PySide2 import QtCore
from tree_item import TreeItem
import nuke

class CustomModel(QtCore.QAbstractItemModel):
    def __init__(self, root_items=None, dir_filePath=None, parent=None):
        super().__init__(parent)
        self.root_item = TreeItem()
        self.dir_filePath = dir_filePath
        
        if root_items:
            for item in root_items:
                self.root_item.appendChild(item)

    def rowCount(self, itemIndex):
        if itemIndex.isValid():
            return len(itemIndex.internalPointer().children)
        else:
            return len(self.root_item.children)

    def columnCount(self, parent=None):
        return 1

    def parent(self, child_index):
        if child_index.isValid():
            item = child_index.internalPointer()
            if item.parent:
                return self.createIndex(item.parent.row(), 0, item.parent)
        return QtCore.QModelIndex()

    def data(self, index, role):
        if not index.isValid():
            return None

        item = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:
            return item.name

    def index(self, row, column, parentIndex=QtCore.QModelIndex()):
        if parentIndex.isValid():
            parent_item = parentIndex.internalPointer()
            return self.createIndex(row, column, parent_item.children[row])
        else:
            return self.createIndex(row, column, self.root_item.children[row])

    def supportedDropActions(self): 
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction         

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled        

    def mimeTypes(self):
        return ['text/xml']

    def mimeData(self, indexes):
        mime_indexes = []
        for index in indexes:
            if index.parent().data() != None:
                for seq in nuke.getFileNameList(f'{self.dir_filePath}/{index.parent().data()}/'):
                        if seq.split('.')[0] == index.data().split('.')[0]:
                            file_path = f'C:/Users/linds/Desktop/nuke_file_browser/fng/{index.parent().data()}/{seq}'
                            mime_indexes.append(file_path)
            else:
                for seq in nuke.getFileNameList(f'{self.dir_filePath}/'):
                        if seq.split('.')[0] == index.data().split('.')[0]:
                            file_path = f'{self.dir_filePath}/{seq}'
                            mime_indexes.append(file_path)

        joined_indexes = ",".join(mime_indexes)
        mimedata = QtCore.QMimeData()
        mimedata.setText(joined_indexes)

        return mimedata

    def dropMimeData(self, data, action, row, column, parent):
        return True