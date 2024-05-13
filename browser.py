from PySide2 import QtWidgets, QtGui, QtCore
import os
import browser_gui
import nuke
import fileseq
from custom_model import CustomModel
from tree_item import TreeItem
import fnmatch

class MyFileBrowser(browser_gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        # self.file_path = None
        self.dir_filePath = "C:/Users/linds/Desktop/nuke_file_browser"
        self.ext_list = ['*.*']
        self.text_filter = '*'
        self.connect_ui()
        self.dir_view_populate()
        self.seq_toggle()

    def connect_ui(self):
        # Connect Checkboxes
        self.sequences_checkbox.clicked.connect(self.seq_toggle)
        self.png_checkbox.clicked.connect(self.create_ext_list)
        self.jpg_checkbox.clicked.connect(self.create_ext_list)
        self.exr_checkbox.clicked.connect(self.create_ext_list)

        # connect clicks in treeViews
        self.dir_view.clicked.connect(self.get_path)

        # Connect line_edit filter
        self.line_edit.textChanged.connect(self.filter_view)

        # Connect Add nodes button
        self.add_nodes_button.clicked.connect(self.add_nodes)

    #populates initial model view default to sequence view
    def dir_view_populate(self):
        path = "C:/Users/linds/Desktop/nuke_file_browser"

        self.dir_model = QtWidgets.QFileSystemModel()
        self.dir_model.setRootPath((QtCore.QDir.rootPath()))
        self.dir_model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        
        self.dir_view.setModel(self.dir_model)
        header = self.dir_view.header()
        header.hideSection(1)
        header.hideSection(2)
        header.hideSection(3)
        self.dir_view.setRootIndex(self.dir_model.index(path))

    # toggle model view from sequence to files
    def seq_toggle(self):
        if (self.sequences_checkbox.isChecked()):
            self.get_sequences()
        else:
            self.update_model()

    # create list of extensions selected by user for filtering
    def create_ext_list(self):
        del self.ext_list[:]
        png_files = self.png_checkbox.isChecked()
        if png_files:
            self.ext_list.append(self.png_checkbox.text())
        jpg_files = self.jpg_checkbox.isChecked()
        if jpg_files:
            self.ext_list.append(self.jpg_checkbox.text())
        exr_files = self.exr_checkbox.isChecked()
        if exr_files:
            self.ext_list.append(self.exr_checkbox.text())
        self.seq_toggle()
    
    # create filter list
    def make_filter_list(self):
        newFilters = []
        if len(self.ext_list) == 0:
            newFilters = [self.text_filter]
        else:
            for filter in self.ext_list:
                newFilters.append(self.text_filter + filter[1:])
        return newFilters
    
    def get_sequences(self):
        # create filter
        filters = self.make_filter_list()
                
        rootItems = []
        # find any sequences in selected dir
        top_seqs = fileseq.findSequencesOnDisk(f'{self.dir_filePath}/*.@.exr', allow_subframes=False)
        if top_seqs:
            for seq in top_seqs:
                    name = seq.__str__().split(seq.dirname())[1]
                    rootItem = TreeItem(name)
                    rootItems.append(rootItem)
        #find sequences in subdirs
        for root, subdirs, files in os.walk(self.dir_filePath):
            for dir in subdirs:
                rootItem = TreeItem(dir)
                rootItems.append(rootItem)
                seqs = fileseq.findSequencesOnDisk(f'{os.path.join(root, dir)}/*.@.exr', allow_subframes=False)
                # if len(seqs) > 0:
                #     print(f'get_item {seqs.__getitem__(0)}')
                for seq in seqs:
                    
                    name = seq.__str__().split(seq.dirname())[1]
                    for pat in filters:
                        if fnmatch.fnmatchcase(name, pat):
                            TreeItem(name, rootItem)                    
        
        # Create & set custom sequence view & model
        self.standard_model = CustomModel(rootItems, self.dir_filePath)
        self.dir_details.setModel(self.standard_model)
        self.dir_details.expandAll()
        self.dir_details.setDragEnabled(True)     

    # update file system model
    def update_model(self):
        self.details_model = QtWidgets.QFileSystemModel()
        self.details_model.setRootPath(QtCore.QDir.rootPath())

        # apply filter to model
        filters = self.make_filter_list()        
        self.details_model.setNameFilters(filters)

        self.details_model.setNameFilterDisables(False)
        self.details_model.directoryLoaded.connect(self.expand_details)
        self.dir_details.setModel(self.details_model)
        self.dir_details.setRootIndex(self.details_model.index(self.dir_filePath)) 
        
    # expand dirs by 1 level after directory is loaded   
    def expand_details(self):
        self.dir_details.expandRecursively(self.details_model.index(self.dir_filePath), 1) 

    # returns the current selected file-path from left side
    def get_path(self):
        self.indexItem = self.dir_view.currentIndex()
        self.dir_filePath = self.dir_model.filePath(self.indexItem)
        
        # Update details_view directory root index
        self.seq_toggle()

    # filter model results by user text input
    def filter_view(self, text):
        if(text != ""):
            self.text_filter = text
        else:
            self.text_filter = "*"
        self.seq_toggle()

    # adds nodes to node graph when 'add nodes' button is clicked
    def add_nodes(self):    
        details_indexItems = self.dir_details.selectionModel().selectedIndexes()
        
        for i in details_indexItems:
            if self.sequences_checkbox.isChecked():
                for seq in nuke.getFileNameList(f'C:/Users/linds/Desktop/nuke_file_browser/fng/{i.parent().data()}/'):
                    if seq.split('.')[0] == i.data().split('.')[0]:
                        file_path = f'C:/Users/linds/Desktop/nuke_file_browser/fng/{i.parent().data()}/{seq}'
                        new_node = nuke.createNode("Read")
                        new_node.knob("file").fromUserText(file_path)
            else:
                if i.column() == 0:
                    file_path = self.details_model.filePath(i)
                    new_node = nuke.createNode("Read")
                    new_node.knob("file").fromUserText(file_path)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()