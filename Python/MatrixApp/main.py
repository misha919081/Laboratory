import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QSplitter, QFrame, QPushButton, QAction, QLineEdit, QGridLayout, QLabel, QSpinBox
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QDoubleValidator

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

        validator = QDoubleValidator()

        MatrixEnter1 = QLineEdit(self.tab1.window1)
        MatrixEnter1.setValidator(validator)
        MatrixEnter2 = QLineEdit(self.tab1.window1)
        MatrixEnter2.setValidator(validator)
        MatrixEnter3 = QLineEdit(self.tab1.window1)
        MatrixEnter3.setValidator(validator)
        MatrixEnter4 = QLineEdit(self.tab1.window1)
        MatrixEnter4.setValidator(validator)
        MatrixEnter5 = QLineEdit(self.tab1.window1)
        MatrixEnter5.setValidator(validator)
        MatrixEnter6 = QLineEdit(self.tab1.window1)
        MatrixEnter6.setValidator(validator)
        MatrixEnter7 = QLineEdit(self.tab1.window1)
        MatrixEnter7.setValidator(validator)
        MatrixEnter8 = QLineEdit(self.tab1.window1)
        MatrixEnter8.setValidator(validator)
        MatrixEnter9 = QLineEdit(self.tab1.window1)
        MatrixEnter9.setValidator(validator)

        MatrixSizeChangerW = QSpinBox(self.tab1.window1)
        MatrixSizeChangerW.setButtonSymbols(0)
        MatrixSizeChangerW.setMinimum(1)
        MatrixSizeChangerW.setMaximum(10)
        MatrixSizeChangerH = QSpinBox(self.tab1.window1)
        MatrixSizeChangerH.setButtonSymbols(0)
        MatrixSizeChangerH.setMinimum(1)
        MatrixSizeChangerH.setMaximum(10)

        Matrix = QGridLayout()
        Matrix.addWidget(MatrixSizeChangerW, 1, 3)
        Matrix.addWidget(MatrixEnter1, 2, 2)
        Matrix.addWidget(MatrixEnter2, 2, 3)
        Matrix.addWidget(MatrixEnter3, 2, 4)
        Matrix.addWidget(MatrixSizeChangerH, 3, 1)
        Matrix.addWidget(MatrixEnter4, 3, 2)
        Matrix.addWidget(MatrixEnter5, 3, 3)
        Matrix.addWidget(MatrixEnter6, 3, 4)
        Matrix.addWidget(MatrixEnter7, 4, 2)
        Matrix.addWidget(MatrixEnter8, 4, 3)
        Matrix.addWidget(MatrixEnter9, 4, 4)
        Matrix.setContentsMargins(35, 10, 65, 185)

        windowContent = QVBoxLayout()
        windowContent.addLayout(labelLayout)
        windowContent.addLayout(Matrix)
        self.tab1.window1.setLayout(windowContent)

        self.tab1.window1.setFrameShape(QFrame.StyledPanel)
        self.tab1.window2 = QFrame(self)
        self.tab1.window2.setFrameShape(QFrame.StyledPanel)
        self.tab1.window3 = QFrame(self)
        self.tab1.window3.setFrameShape(QFrame.StyledPanel)

        # Create splitter for run and description windows
        self.tab1.description = QSplitter(Qt.Vertical)
        self.tab1.description.addWidget(self.tab1.window2)
        self.tab1.description.addWidget(self.tab1.window3)
        self.tab1.description.setSizes([450, 200])

        #Create splitter for all windows
        self.tab1.content = QSplitter(Qt.Horizontal)
        self.tab1.content.addWidget(self.tab1.window1)
        self.tab1.content.addWidget(self.tab1.description)
        self.tab1.content.setSizes([550, 400])

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

# Running application
if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Run()
    sys.exit(app.exec_())
