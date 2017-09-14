import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QSplitter, QFrame, QPushButton, QAction, QLineEdit, QGridLayout, QLabel
from PyQt5.QtCore import pyqtSlot, Qt

class Run(QWidget):

    def __init__(self):  # Class initialization
        super().__init__()

        self.initUI()

    def initUI(self):  # GUI initialization
        self.resize(1000, 600)
        self.center()

        self.tab_widget = Tab_Widget(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)
        # self.setCentralWidget(self.tab_widget)  # Addition tab list in main window

        self.show()  #Show application

    def center(self):  # Set central position for window
        frame = self.frameGeometry()
        mid = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(mid)
        self.move(frame.topLeft())

    def exit(self):
        self.close()

class Tab_Widget(Run):

    def __init__(self, parent):  # Class initialization
        super(Run, self).__init__(parent)
        layout = QVBoxLayout()

        # Create tab list
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        #Addition tabs in list
        self.tabs.addTab(self.tab1, "Детерминант")
        self.tabs.addTab(self.tab2, "Умножение матриц")
        self.tabs.addTab(self.tab3, "Решение систем линейных уравнений(правило Крамера)")

        # Create first tab
        # Create 3 basic window as QFrame
        self.tab1.window1 = QFrame(self)

        label = QLabel('Введите матрицу')
        labelLayout = QVBoxLayout()
        labelLayout.addWidget(label, 0, Qt.AlignHCenter)

        MatrixEnter1 = QLineEdit(self.tab1.window1)
        MatrixEnter2 = QLineEdit(self.tab1.window1)
        MatrixEnter3 = QLineEdit(self.tab1.window1)
        MatrixEnter4 = QLineEdit(self.tab1.window1)
        MatrixEnter5 = QLineEdit(self.tab1.window1)
        MatrixEnter6 = QLineEdit(self.tab1.window1)
        MatrixEnter7 = QLineEdit(self.tab1.window1)
        MatrixEnter8 = QLineEdit(self.tab1.window1)
        MatrixEnter9 = QLineEdit(self.tab1.window1)

        Matrix = QGridLayout()
        Matrix.addWidget(MatrixEnter1, 1, 1)
        Matrix.addWidget(MatrixEnter2, 1, 2)
        Matrix.addWidget(MatrixEnter3, 1, 3)
        Matrix.addWidget(MatrixEnter4, 2, 1)
        Matrix.addWidget(MatrixEnter5, 2, 2)
        Matrix.addWidget(MatrixEnter6, 2, 3)
        Matrix.addWidget(MatrixEnter7, 3, 1)
        Matrix.addWidget(MatrixEnter8, 3, 2)
        Matrix.addWidget(MatrixEnter9, 3, 3)
        Matrix.setContentsMargins(180, 200, 180, 200)

        windowContent = QVBoxLayout()
        windowContent.addLayout(labelLayout)
        windowContent.addLayout(Matrix)
        self.tab1.window1.setLayout(windowContent)

        # button = QPushButton('Close', self.tab1.window1)
        # button.setCheckable(True)
        # button.move(300, 300)
        # button.clicked.connect(self.exitAction)
        self.tab1.window1.setFrameShape(QFrame.StyledPanel)
        self.tab1.window2 = QFrame(self)
        self.tab1.window2.setFrameShape(QFrame.StyledPanel)
        self.tab1.window3 = QFrame(self)
        self.tab1.window3.setFrameShape(QFrame.StyledPanel)

        # Create splitter for run and description windows
        self.tab1.description = QSplitter(Qt.Vertical)
        self.tab1.description.addWidget(self.tab1.window2)
        self.tab1.description.addWidget(self.tab1.window3)
        self.tab1.description.setSizes([400, 200])

        #Create splitter for all windows
        self.tab1.content = QSplitter(Qt.Horizontal)
        self.tab1.content.addWidget(self.tab1.window1)
        self.tab1.content.addWidget(self.tab1.description)
        self.tab1.content.setSizes([600, 400])

        # Addition splitter in tab
        self.tab1.layout = QHBoxLayout()
        self.tab1.layout.addWidget(self.tab1.content)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        # Create 3 basic window as QFrame
        self.tab2.window1 = QFrame(self)
        self.tab2.window1.setFrameShape(QFrame.StyledPanel)
        self.tab2.window2 = QFrame(self)
        self.tab2.window2.setFrameShape(QFrame.StyledPanel)
        self.tab2.window3 = QFrame(self)
        self.tab2.window3.setFrameShape(QFrame.StyledPanel)

        # Create splitter for run and description windows
        self.tab2.description = QSplitter(Qt.Vertical)
        self.tab2.description.addWidget(self.tab2.window2)
        self.tab2.description.addWidget(self.tab2.window3)
        self.tab2.description.setSizes([400, 200])

        #Create splitter for all windows
        self.tab2.content = QSplitter(Qt.Horizontal)
        self.tab2.content.addWidget(self.tab2.window1)
        self.tab2.content.addWidget(self.tab2.description)
        self.tab2.content.setSizes([600, 400])

        # Addition splitter in tab
        self.tab2.layout = QHBoxLayout(self)
        self.tab2.layout.addWidget(self.tab2.content)
        self.tab2.setLayout(self.tab2.layout)

        # Create third tab
        # Create 3 basic window as QFrame
        self.tab3.window1 = QFrame(self)
        self.tab3.window1.setFrameShape(QFrame.StyledPanel)
        self.tab3.window2 = QFrame(self)
        self.tab3.window2.setFrameShape(QFrame.StyledPanel)
        self.tab3.window3 = QFrame(self)
        self.tab3.window3.setFrameShape(QFrame.StyledPanel)

        # Create splitter for run and description windows
        self.tab3.description = QSplitter(Qt.Vertical)
        self.tab3.description.addWidget(self.tab3.window2)
        self.tab3.description.addWidget(self.tab3.window3)
        self.tab3.description.setSizes([400, 200])

        #Create splitter for all windows
        self.tab3.content = QSplitter(Qt.Horizontal)
        self.tab3.content.addWidget(self.tab3.window1)
        self.tab3.content.addWidget(self.tab3.description)
        self.tab3.content.setSizes([600, 400])

        # Addition splitter in tab
        self.tab3.layout = QHBoxLayout(self)
        self.tab3.layout.addWidget(self.tab3.content)
        self.tab3.setLayout(self.tab3.layout)

        # Addition tab list in layout for main window
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    # def exitAction(self):
    #     self.close()

# Running application
if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Run()
    sys.exit(app.exec_())
