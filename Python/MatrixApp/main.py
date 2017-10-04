import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QSplitter, QFrame, QPushButton, QAction, QLineEdit, QGridLayout, QLabel, QSpinBox, QDoubleSpinBox)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QDoubleValidator
from numpy import linalg

class Run(QWidget):

    def __init__(self):  # Class initialization
        super().__init__()

        self.initUI()

    def initUI(self):  # initialization
        self.resize(1000, 600)
        self.center()

        tab_widget = Tab_Widget()
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

        self.setWindowTitle('Matrix handler v. 0.0.4')

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

        self.tab1.label = QLabel('Введите матрицу')

        self.tab1.tabM = self.MatrixGenerate()

        self.tab1.labelLayout = QVBoxLayout()
        self.tab1.labelLayout.addWidget(self.tab1.label, 0, Qt.AlignHCenter)
        self.tab1.labelLayout.addWidget(QSpinBox(), 0, Qt.AlignHCenter)

        self.tab1.MatrixField = QGridLayout()
        self.tab1.MatrixField.addWidget(QSpinBox(), 1, 2)
        self.tab1.MatrixField.addWidget(QSpinBox(), 2, 1)
        self.tab1.MatrixField.addLayout(self.tab1.tabM, 2, 2)
        self.tab1.MatrixField.setAlignment(Qt.AlignCenter)
        item = self.tab1.MatrixField.itemAt(0)
        item.widget().setValue(3)
        item.widget().setButtonSymbols(0)
        item.widget().setRange(1, 10)
        item.widget().valueChanged.connect(self.changesize)
        item = self.tab1.labelLayout.itemAt(1)
        item.widget().setValue(3)
        item.widget().setButtonSymbols(0)
        item.widget().setRange(1, 10)
        item.widget().valueChanged.connect(self.changesize)

        self.tab1.window1Content = QVBoxLayout()
        self.tab1.window1Content.addLayout(self.tab1.labelLayout)
        self.tab1.window1Content.addLayout(self.tab1.MatrixField)
        self.tab1.window1Content.setAlignment(Qt.AlignCenter)
        self.tab1.window1.setLayout(self.tab1.window1Content)

        self.tab1.window1.setFrameShape(QFrame.StyledPanel)
#======================================================================================================================#

        self.tab1.window2 = QFrame(self)

        self.tab1.title = QLabel('Детерминант матрицы')
        self.tab1.title.setAlignment(Qt.AlignCenter)
        self.tab1.determinantLabel = QLabel('Для определения детерминанта матрицы данная программа использует следующую формулу:')
        self.tab1.determinantLabel.setAlignment(Qt.AlignCenter)

        self.tab1.window2Content = QVBoxLayout()
        self.tab1.window2Content.addWidget(self.tab1.title)
        self.tab1.window2Content.addWidget(self.tab1.determinantLabel)
        self.tab1.window2Content.setAlignment(Qt.AlignCenter)
        self.tab1.window2.setLayout(self.tab1.window2Content)

        self.tab1.window2.setFrameShape(QFrame.StyledPanel)
#======================================================================================================================#

        self.tab1.window3 = QFrame(self)

        self.tab1.startButton = QPushButton('Рассчитать')
        self.tab1.startButton.clicked.connect(self.determinant)
        self.tab1.resetButton = QPushButton('Очистить матрицу')
        self.tab1.resetButton.clicked.connect(self.clearMatrix)

        self.tab1.window3Content = QHBoxLayout()
        self.tab1.window3Content.addWidget(self.tab1.startButton)
        self.tab1.window3Content.addWidget(self.tab1.resetButton)
        self.tab1.window3Content.setAlignment(Qt.AlignCenter)
        self.tab1.window3.setLayout(self.tab1.window3Content)

        self.tab1.window3.setFrameShape(QFrame.StyledPanel)
# ======================================================================================================================#

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

        for i in range(3):
            for g in range(3):
                self.Matrix.addWidget(QDoubleSpinBox(), i, g)

        k = 0
        for i in range(9):
            item = self.Matrix.itemAt(k)
            item.widget().setButtonSymbols(2)
            item.widget().setRange(-100000.000000, 100000.000000)
            k += 1

        return self.Matrix

    def changesize(self):

        row = 3
        column = 3

        while (self.Matrix.count()):
            item = self.Matrix.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for i in range(row):
            for g in range(column):
                self.Matrix.addWidget(QDoubleSpinBox(), i, g)

        k = 0
        for i in range(row * column):
            item = self.Matrix.itemAt(k)
            item.widget().setButtonSymbols(2)
            item.widget().setRange(-100000.000000, 100000.000000)
            k += 1

    def determinant(self):

        MatrixData = []
        row = []
        k = 0

        for i in range(self.Matrix.rowCount()):
            for g in range(self.Matrix.columnCount()):
                item = self.Matrix.itemAt(k)
                row.append(item.widget().value())
                k += 1
            MatrixData.append([])
            MatrixData[i].extend(row)
            row.clear()

        self.result = QWidget()
        self.result.setWindowTitle('Результаты расчетов')
        self.result.resize(400, 130)
        label = QLabel('Детерминант матрицы равен: ' + str(linalg.det(MatrixData)), self.result)
        label.setAlignment(Qt.AlignCenter)
        label.move(85, 60)

        frame = self.result.frameGeometry()
        mid = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(mid)
        self.result.move(frame.topLeft())

        self.result.show()

    def clearMatrix(self):

        for i in range(self.Matrix.rowCount() * self.Matrix.columnCount()):
            item = self.Matrix.itemAt(i)
            item.widget().setValue(0.0)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Run()
    sys.exit(app.exec_())
