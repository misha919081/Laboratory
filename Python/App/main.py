import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Pattern(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(1000, 600)
        self.center()

        exitAction = QAction(QIcon('exit24.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        tools = self.addToolBar('Exit')
        tools.addAction(exitAction)

        self.setWindowTitle('My App')
        self.show()

    def center(self):

        frame = self.frameGeometry()
        mid = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(mid)
        self.move(frame.topLeft())

if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Pattern()
    sys.exit(app.exec_())
