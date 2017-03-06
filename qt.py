import sys
from PyQt4 import QtGui, QtCore

##app = QtGui.QApplication(sys.argv)
##
##window = QtGui.QWidget()
##window.setGeometry(100, 100, 500, 300)
##window.setWindowTitle("Kushal")
##
##window.show()

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 200, 500, 300)
        self.setWindowTitle("kushal")
##        self.setWindowIcon(QtGui.QIcon(r'C:\Users\Admin\Pictures\Wallpapers\Dim Graveyard.png'))
##
##        openEditor = QtGui.QAction("Editor", self)
##        openEditor.setShortcut("Ctrl+E")
##        openEditor.triggered.connect(self.editor)
##        
##        extractAction1 = QtGui.QAction("New File", self)
##        extractAction1.setShortcut("Ctrl+N")
##        extractAction1.setStatusTip("New")
##        extractAction1.triggered.connect(self.close_application)
##
##        extractAction2 = QtGui.QAction("Exit", self)
##        extractAction2.setShortcut("Ctrl+Q")
##        extractAction2.setStatusTip("Leave the App")
##        extractAction2.triggered.connect(self.close_application)
##
##        extractAction3 = QtGui.QAction("Undo", self)
##        extractAction3.setShortcut("Ctrl+Z")
##        extractAction3.setStatusTip("Undo")
##        extractAction3.triggered.connect(self.close_application)
##
##        extractAction4 = QtGui.QAction("Undo", self)
##        extractAction4.setShortcut("Ctrl+Z")
##        extractAction4.setStatusTip("Undo")
##        extractAction4.triggered.connect(self.close_application)
##        
##        extractAction5 = QtGui.QAction("comment out", self)
##        extractAction5.setShortcut("Alt+3")
##        extractAction5.setStatusTip("Comment out")
##        extractAction5.triggered.connect(self.close_application)
##
##        extractAction6 = QtGui.QAction("Uncomment", self)
##        extractAction6.setShortcut("Alt+4")
##        extractAction6.setStatusTip("Uncomment")
##        extractAction6.triggered.connect(self.close_application)
##
##      
##        
##        self.statusBar()
##
##        mainMenu = self.menuBar()
##        fileMenu1 = mainMenu.addMenu('File')
##        fileMenu1.addAction(extractAction1)
##        fileMenu1.addAction(extractAction2)
##
##        fileMenu2 = mainMenu.addMenu("Edit")
##        fileMenu2.addAction(extractAction3)
##        fileMenu2.addAction(extractAction4)
##
##        
##        fileMenu2 = mainMenu.addMenu("Format")
##        fileMenu2.addAction(extractAction5)
##        fileMenu2.addAction(extractAction6)
##
##        fileMenu2 = mainMenu.addMenu("Editor")
##        fileMenu2.addAction(openEditor)
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

##        extractAction = QtGui.QAction(QtGui.QIcon(r'C:\Users\Admin\Pictures\Wallpapers\Dim Graveyard.png'), 'Graveyard', self)
##        extractAction.setStatusTip("Uncomment")
##        extractAction.setShortcut("Alt+7")
##        extractAction.triggered.connect(self.close_application)
##        
##        toolBar = self.addToolBar("Extraction")
##        toolBar.addAction(extractAction)
##
##        checkBox = QtGui.QCheckBox("Enlarge Window", self)
##        checkBox.move(100, 100)
##        checkBox.toggle()
##        checkBox.stateChanged.connect(self.enlarge_window)
##
##        self.progress = QtGui.QProgressBar(self)
##        self.progress.setGeometry(200, 80, 250, 20)
##        btn = QtGui.QPushButton("Download", self)
##        btn.move(200, 120)
##        btn.clicked.connect(self.download)
##
##        print(self.style().objectName())
##        #styleChoice = QtGui.QLabel("Windows Vista", self)
##        #comboox = 9826342557
        self.show()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked :
            self.setGeometry(100, 100, 1000, 600)
        else:
            self.setGeometry(100, 100, 500, 300)

    def download(self):
        completed = 0
        while completed < 100:
            completed += 0.0001
            self.progress.setValue(completed)

    def editor(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "quit", "you sure?",
                                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
            

def run():
    app = QtGui.QApplication(sys.argv)

    GUI = Window()
    sys.exit(app.exec_())

run()
