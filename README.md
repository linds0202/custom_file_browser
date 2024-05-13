# custom_file_browser

# A customer file browser tool built with PySide2 and Qt Designer.

Problem: Nuke only allows selection of files/sequences from a single directory. This requires artists to waste time repetitively opening the file browser to place nodes into the node graph.

Solution: File browser tool with a QFileSystem tree view/model on the left and a custom tree view model on the right that allows artists to select files/sequences from multiple directories.

# The custom tool also allows:
#  - Toggle between sequence and file view
#  - Filter by text
#  - Filter by file extension
#  - Filter by text & file extension combo
#  - Drag and drop selected nodes in Node Graph
#  - “Add nodes” button to place selected nodes into the Node Graph

