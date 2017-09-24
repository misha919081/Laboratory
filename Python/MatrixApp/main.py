import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QSplitter, QFrame, QPushButton, QAction, QLineEdit, QGridLayout, QLabel, QSpinBox)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QDoubleValidator

class Run(QWidget):

    def __init__(self):  # Class initialization
        super().__init__()

        self.initUI()

    def initUI(self):  # GUI initialization
        self.resize(1920, 1080)
        self.center()

        tab_widget = Tab_Widget()
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

        self.setWindowTitle('Matrix handler v. 0.0.0')

        self.show()  #Show application

    def center(self):  # Set central position for window
        frame = self.frameGeometry()
        mid = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(mid)
        self.move(frame.topLeft())

class Tab_Widget(QWidget):

    def __init__(self):  # Class initialization
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create tab list
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Addition tabs in list
        self.tabs.addTab(self.tab1, "Детерминант")
        self.tabs.addTab(self.tab2, "Умножение матриц")
        self.tabs.addTab(self.tab3, "Решение систем линейных уравнений(правило Крамера)")

        # Create first tab
        # Create 3 basic window as QFrame
        self.tab1.window1 = QFrame(self)

        tabM = Matrix()

        label = QLabel('Введите матрицу')

        MatrixSizeChangerW = QSpinBox(self.tab1.window1)
        MatrixSizeChangerW.setButtonSymbols(0)
        MatrixSizeChangerW.setMinimum(1)
        MatrixSizeChangerW.setMaximum(10)
        MatrixSizeChangerW.valueChanged.connect(tabM.changeMatrixWidth)
        MatrixSizeChangerH = QSpinBox(self.tab1.window1)
        MatrixSizeChangerH.setButtonSymbols(0)
        MatrixSizeChangerH.setMinimum(1)
        MatrixSizeChangerH.setMaximum(10)
        MatrixSizeChangerH.valueChanged.connect(tabM.changeMatrixHeight)

        labelLayout = QVBoxLayout()
        labelLayout.addWidget(label, 0, Qt.AlignHCenter)
        labelLayout.addWidget(MatrixSizeChangerW, 0, Qt.AlignHCenter)

        MatrixField = QGridLayout()
        MatrixField.addWidget(MatrixSizeChangerH, 1, 1)
        MatrixField.addLayout(tabM, 1, 2)
        MatrixField.setAlignment(Qt.AlignCenter)

        windowContent = QVBoxLayout()
        windowContent.addLayout(labelLayout)
        windowContent.addLayout(MatrixField)
        windowContent.setAlignment(Qt.AlignCenter)
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
        self.tab1.description.setSizes([1050, 400])

        # Create splitter for all windows
        self.tab1.content = QSplitter(Qt.Horizontal)
        self.tab1.content.addWidget(self.tab1.window1)
        self.tab1.content.addWidget(self.tab1.description)
        self.tab1.content.setSizes([870, 680])

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

        # Create splitter for all windows
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

        # Create splitter for all windows
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

class Matrix(QGridLayout):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        MatrixEnter = []
        validator = QDoubleValidator()

        for i in range(9):
            MatrixEnter.append(QLineEdit())
            MatrixEnter[i].setValidator(validator)

        count = 0
        for i in range(3):
            for j in range(3):
                self.addWidget(MatrixEnter[count], i, j)
                count += 1

    def changeMatrixHeight(self):

        MatrixExpand = []
        validator = QDoubleValidator()

        size_parameter = self.rowCount()

        for i in range(self.columnCount()):
            MatrixExpand.append(QLineEdit())
            MatrixExpand[i].setValidator(validator)
            self.addWidget(MatrixExpand[i], size_parameter, i)

    def changeMatrixWidth(self):

        MatrixExpand = []
        validator = QDoubleValidator()

        size_patameter = self.columnCount()

        for i in range(self.rowCount()):
            MatrixExpand.append(QLineEdit())
            MatrixExpand[i].setValidator(validator)
            self.addWidget(MatrixExpand[i], i, size_patameter)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Run()
    sys.exit(app.exec_())
