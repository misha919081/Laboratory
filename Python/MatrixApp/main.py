import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QSplitter, QFrame, QPushButton, QAction, QLineEdit, QGridLayout, QLabel, QSpinBox)
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
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

        self.setWindowTitle('Matrix handler v. 0.0.2.1')

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
########################################################################################################################
#======================================================================================================================#
        self.tab1.window1 = QFrame(self)

        label = QLabel('Введите матрицу')

        self.MatrixSizeChangerW = QSpinBox()
        self.MatrixSizeChangerW.setValue(3)
        self.MatrixSizeChangerW.setButtonSymbols(0)
        self.MatrixSizeChangerW.setMinimum(1)
        self.MatrixSizeChangerW.setMaximum(10)
        self.MatrixSizeChangerW.valueChanged.connect(self.changeMatrixWidth)
        self.MatrixSizeChangerH = QSpinBox()
        self.MatrixSizeChangerH.setValue(3)
        self.MatrixSizeChangerH.setButtonSymbols(0)
        self.MatrixSizeChangerH.setMinimum(1)
        self.MatrixSizeChangerH.setMaximum(10)
        # self.MatrixSizeChangerH.valueChanged.connect(self.changeMatrixHeight)

        tabM = self.MatrixGenerate()

        labelLayout = QVBoxLayout()
        labelLayout.addWidget(label, 0, Qt.AlignHCenter)
        labelLayout.addWidget(self.MatrixSizeChangerW, 0, Qt.AlignHCenter)

        MatrixField = QGridLayout()
        MatrixField.addWidget(self.MatrixSizeChangerH, 1, 1)
        MatrixField.addLayout(tabM, 1, 2)
        MatrixField.setAlignment(Qt.AlignCenter)

        window1Content = QVBoxLayout()
        window1Content.addLayout(labelLayout)
        window1Content.addLayout(MatrixField)
        window1Content.setAlignment(Qt.AlignCenter)
        self.tab1.window1.setLayout(window1Content)

        self.tab1.window1.setFrameShape(QFrame.StyledPanel)

#======================================================================================================================#

        self.tab1.window2 = QFrame(self)

        title = QLabel('Детерминант матрицы')
        title.setAlignment(Qt.AlignCenter)
        determinantLabel = QLabel('Для определения детерминанта матрицы данная программа использует следующую формулу:')
        determinantLabel.setAlignment(Qt.AlignCenter)

        window2Content = QVBoxLayout()
        window2Content.addWidget(title)
        window2Content.addWidget(determinantLabel)
        window2Content.setAlignment(Qt.AlignCenter)
        self.tab1.window2.setLayout(window2Content)

        self.tab1.window2.setFrameShape(QFrame.StyledPanel)

#======================================================================================================================#

        self.tab1.window3 = QFrame(self)

        startButton = QPushButton('Рассчитать')
        resetButton = QPushButton('Очистить матрицу')

        window3Content = QHBoxLayout()
        window3Content.addWidget(startButton)
        window3Content.addWidget(resetButton)
        window3Content.setAlignment(Qt.AlignCenter)
        self.tab1.window3.setLayout(window3Content)

        self.tab1.window3.setFrameShape(QFrame.StyledPanel)

        # Create splitter for run and description windows
        description = QSplitter(Qt.Vertical)
        description.addWidget(self.tab1.window2)
        description.addWidget(self.tab1.window3)
        description.setSizes([1050, 400])

        # Create splitter for all windows
        content = QSplitter(Qt.Horizontal)
        content.addWidget(self.tab1.window1)
        content.addWidget(description)
        content.setSizes([870, 680])

        # Addition splitter in tab
        tab1Content = QHBoxLayout()
        tab1Content.addWidget(content)
        self.tab1.setLayout(tab1Content)

########################################################################################################################
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

########################################################################################################################
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
########################################################################################################################

        # Addition tab list in layout for main window
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def MatrixGenerate(self):

        self.Matrix = QGridLayout()
        self.MatrixEnter = [[], [], [], [], [], [], [], [], [], []]
        validator = QDoubleValidator()

        for i in range(10):
            for g in range(10):
                self.MatrixEnter[i].append(QLineEdit())
                self.MatrixEnter[i][g].setValidator(validator)

        for i in range(self.MatrixSizeChangerH.value()):
            for g in range(self.MatrixSizeChangerW.value()):
                self.Matrix.addWidget(self.MatrixEnter[i][g], i, g)

        return self.Matrix

    def changeMatrixHeight(self):

        if self.MatrixSizeChangerH.value() > self.Matrix.rowCount():
            row = self.MatrixSizeChangerH.value()
            for i in range(self.Matrix.columnCount()):
                self.Matrix.addWidget(self.MatrixEnter[i][row - 1], i, self.MatrixSizeChangerH.value() - 1)

    def changeMatrixWidth(self):

        if self.MatrixSizeChangerW.value() > self.Matrix.columnCount():
            column = self.MatrixSizeChangerW.value()
            for i in range(self.Matrix.rowCount()):
                self.Matrix.addWidget(self.MatrixEnter[column - 1][i], i, self.MatrixSizeChangerW.value() - 1)
        elif self.MatrixSizeChangerW.value() < self.Matrix.columnCount():
            column = self.MatrixSizeChangerW.value()
            for i in range(self.Matrix.rowCount()):
                self.Matrix.removeWidget(self.MatrixEnter[i][column - 1])


if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Run()
    sys.exit(app.exec_())
