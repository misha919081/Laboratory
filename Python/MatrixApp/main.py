import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QDesktopWidget, QVBoxLayout, \
    QHBoxLayout, QSplitter, QFrame, QPushButton, QAction, QLineEdit, QGridLayout, QLabel, QSpinBox, QDoubleSpinBox)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QDoubleValidator
from numpy import linalg, dot

class Run(QWidget):

    def __init__(self):  # Class initialization
        super().__init__()

        self.initUI()

    def initUI(self):  # initialization
        self.resize(1600, 900)
        self.center()

        tab_widget = Tab_Widget()
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

        self.setWindowTitle('Matrix handler v. 0.3.0')

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
        self.tabs.addTab(self.tab3, "Решение систем линейных уравнений")

        # Create first tab
        # Create 3 basic window as QFrame
########################################################################################################################
# ==================================================================================================================== #
        self.tab1.window1 = QFrame(self)

        self.tab1.label = QLabel('Введите матрицу')
        self.tab1.MatrixField = QVBoxLayout()
        self.tab1.MatrixField.addWidget(self.tab1.label, 0, Qt.AlignHCenter)
        self.tab1.MatrixField.addWidget(Matrix(type=0))
        self.tab1.MatrixField.setAlignment(Qt.AlignCenter)
        self.tab1.window1.setLayout(self.tab1.MatrixField)

        self.tab1.window1.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

        self.tab1.window2 = QFrame(self)

        self.tab1.window2Content = QVBoxLayout()
        self.tab1.window2Content.addWidget(QLabel('Детерминант матрицы'))
        self.tab1.window2Content.addWidget(QLabel('Рассчет детерминанта матрицы производится по следующей формуле:'))
        self.tab1.window2Content.itemAt(0).widget().setAlignment(Qt.AlignCenter)
        self.tab1.window2Content.itemAt(1).widget().setAlignment(Qt.AlignCenter)
        self.tab1.window2Content.setAlignment(Qt.AlignCenter)
        self.tab1.window2.setLayout(self.tab1.window2Content)

        self.tab1.window2.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

        self.tab1.window3 = QFrame(self)

        self.tab1.startButton = QPushButton('Рассчитать')
        self.tab1.startButton.clicked.connect(self.tab1.MatrixField.itemAt(1).widget().determinant)
        self.tab1.resetButton = QPushButton('Очистить матрицу')
        self.tab1.resetButton.clicked.connect(self.tab1.MatrixField.itemAt(1).widget().clearMatrix)

        self.tab1.window3Content = QHBoxLayout()
        self.tab1.window3Content.addWidget(self.tab1.startButton)
        self.tab1.window3Content.addWidget(self.tab1.resetButton)
        self.tab1.window3Content.setAlignment(Qt.AlignCenter)
        self.tab1.window3.setLayout(self.tab1.window3Content)

        self.tab1.window3.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

        # Create splitter for run and description windows
        self.tab1.description = QSplitter(Qt.Vertical)
        self.tab1.description.addWidget(self.tab1.window2)
        self.tab1.description.addWidget(self.tab1.window3)
        self.tab1.description.setSizes([400, 200])

        # Create splitter for all windows
        self.tab1.content = QSplitter(Qt.Horizontal)
        self.tab1.content.addWidget(self.tab1.window1)
        self.tab1.content.addWidget(self.tab1.description)
        self.tab1.content.setSizes([600, 400])

        # Addition splitter in tab
        self.tab1.tab1Content = QHBoxLayout()
        self.tab1.tab1Content.addWidget(self.tab1.content)
        self.tab1.setLayout(self.tab1.tab1Content)

########################################################################################################################
# ==================================================================================================================== #
        # Create second tab
        # Create 3 basic window as QFrame
        self.tab2.window1 = QFrame(self)

        self.tab2.MatrixField1 = QVBoxLayout()
        self.tab2.MatrixField1.addWidget(QLabel('Введите матрицу'), 0, Qt.AlignHCenter)
        self.tab2.MatrixField1.addWidget(Matrix(type=0))
        self.tab2.MatrixField1.setAlignment(Qt.AlignCenter)

        self.tab2.MatrixField2 = QVBoxLayout()
        self.tab2.MatrixField2.addWidget(QLabel('Введите матрицу'), 0, Qt.AlignHCenter)
        self.tab2.MatrixField2.addWidget(Matrix(type=0))
        self.tab2.MatrixField2.setAlignment(Qt.AlignCenter)

        self.tab2.window1Content = QHBoxLayout()
        self.tab2.window1Content.addLayout(self.tab2.MatrixField1, Qt.AlignHCenter)
        self.tab2.window1Content.addLayout(self.tab2.MatrixField2, Qt.AlignHCenter)
        # self.tab2.window1Content.setAlignment(Qt.AlignCenter)
        self.tab2.window1.setLayout(self.tab2.window1Content)

        self.tab2.window1.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

        self.tab2.window2 = QFrame(self)
        self.label = QLabel('ВНИМАНИЕ!!!! При умножении матриц, помните, что\n число строк в 1 матрице и число '
                            'столбцов во \n второй матрице должны СОВПАДАТЬ!\n В дальнейшем будет добавлено оповещение,\n'
                            'выводящее ошибку при попытке умножения\n без соблюдения этого правила.', self.tab2.window2)
        self.tab2.window2.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

        self.tab2.window3 = QFrame(self)
        self.startButton = QPushButton('Рассчитать', self.tab2.window3)
        self.startButton.clicked.connect(self.MatrixMultiple)
        self.tab2.window3.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

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
        self.tab2.layout = QHBoxLayout()
        self.tab2.layout.addWidget(self.tab2.content)
        self.tab2.setLayout(self.tab2.layout)

########################################################################################################################
# ==================================================================================================================== #
        # Create third tab
        # Create 3 basic window as QFrame
        self.tab3.window1 = QFrame(self)

        self.tab3.MatrixField = QVBoxLayout()
        self.tab3.MatrixField.addWidget(QLabel('Введите матрицу'), 0, Qt.AlignHCenter)
        self.tab3.MatrixField.addWidget(Matrix(type=1))
        self.tab3.MatrixField.setAlignment(Qt.AlignCenter)
        self.tab3.window1.setLayout(self.tab3.MatrixField)

        self.tab3.window1.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

        self.tab3.window2 = QFrame(self)
        self.tab3.window2.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #
        self.tab3.window3 = QFrame(self)
        self.tab1.startButton = QPushButton('Рассчитать', self.tab3.window3)
        self.tab1.startButton.clicked.connect(self.tab3.MatrixField.itemAt(1).widget().linEquation)
        self.tab3.window3.setFrameShape(QFrame.StyledPanel)
# ==================================================================================================================== #

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

    def MatrixMultiple(self):
        MatrixData1 = []
        MatrixData2 = []
        row = []

        k = 0
        for i in range(self.tab2.MatrixField1.itemAt(1).widget().MatrixConstructor.itemAt(1).widget().value()):
            for g in range(self.tab2.MatrixField1.itemAt(1).widget().MatrixConstructor.itemAt(0).widget().value()):
                item = self.tab2.MatrixField1.itemAt(1).widget().MatrixGrid.itemAt(k)
                row.append(item.widget().value())
                k += 1
            MatrixData1.append([])
            MatrixData1[i].extend(row)
            row.clear()

        k = 0
        for i in range(self.tab2.MatrixField2.itemAt(1).widget().MatrixConstructor.itemAt(1).widget().value()):
            for g in range(self.tab2.MatrixField2.itemAt(1).widget().MatrixConstructor.itemAt(0).widget().value()):
                item = self.tab2.MatrixField2.itemAt(1).widget().MatrixGrid.itemAt(k)
                row.append(item.widget().value())
                k += 1
            MatrixData2.append([])
            MatrixData2[i].extend(row)
            row.clear()

        self.result = QWidget()
        self.result.setWindowTitle('Результаты расчетов')
        self.result.resize(400, 130)
        label = QLabel('x = ' + str(dot(MatrixData1, MatrixData2)), self.result)
        label.setAlignment(Qt.AlignCenter)
        label.move(85, 60)

        frame = self.result.frameGeometry()
        mid = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(mid)
        self.result.move(frame.topLeft())

        self.result.show()

class Matrix(QWidget):

    def __init__(self, type):
        super(QWidget, self).__init__()

        if type == 0:
            self.MatrixConstructor = QGridLayout()
            self.MatrixConstructor.addWidget(QSpinBox(), 1, 2, Qt.AlignHCenter)
            self.MatrixConstructor.addWidget(QSpinBox(), 2, 1, Qt.AlignHCenter)
            self.MatrixConstructor.addLayout(self.MatrixGenerate(), 2, 2)
            self.MatrixConstructor.itemAt(0).widget().setRange(1, 10)
            self.MatrixConstructor.itemAt(1).widget().setRange(1, 10)
            self.MatrixConstructor.itemAt(0).widget().setValue(3)
            self.MatrixConstructor.itemAt(1).widget().setValue(3)
            item = self.MatrixConstructor.itemAt(0)
            item.widget().valueChanged.connect(self.changesize)
            item = self.MatrixConstructor.itemAt(1)
            item.widget().valueChanged.connect(self.changesize)
            self.MatrixConstructor.setAlignment(Qt.AlignCenter)
            self.setLayout(self.MatrixConstructor)

        elif type == 1:
            self.MatrixConstructor = QGridLayout()
            self.MatrixBase = QGridLayout()
            self.MatrixBase.addWidget(QSpinBox(), 1, 2, Qt.AlignHCenter)
            self.MatrixBase.addWidget(QSpinBox(), 2, 1, Qt.AlignHCenter)
            self.MatrixBase.addLayout(self.MatrixGenerate(), 2, 2)
            self.MatrixBase.itemAt(0).widget().setRange(1, 10)
            self.MatrixBase.itemAt(1).widget().setRange(1, 10)
            self.MatrixBase.itemAt(0).widget().setValue(3)
            self.MatrixBase.itemAt(1).widget().setValue(3)
            item = self.MatrixBase.itemAt(0)
            item.widget().valueChanged.connect(self.changesize)
            item = self.MatrixBase.itemAt(1)
            item.widget().valueChanged.connect(self.changesize)
            self.MatrixBase.setAlignment(Qt.AlignCenter)

            self.MatrixValues = QVBoxLayout()
            for i in range(self.MatrixBase.itemAt(1).widget().value()):
                self.MatrixValues.addWidget(QDoubleSpinBox())
                self.MatrixValues.itemAt(i).widget().setButtonSymbols(2)
                self.MatrixValues.itemAt(i).widget().setRange(-100000.000000, 100000.000000)

            self.MatrixBig = QHBoxLayout()
            self.MatrixBig.addLayout(self.MatrixBase)
            self.MatrixBig.addLayout(self.MatrixValues)
            self.MatrixBig.setAlignment(Qt.AlignHCenter)
            self.setLayout(self.MatrixBig)

    def MatrixGenerate(self):
        self.MatrixGrid = QGridLayout()

        for i in range(3):
            for g in range(3):
                self.MatrixGrid.addWidget(QDoubleSpinBox(), i, g, Qt.AlignHCenter)

        k = 0
        for i in range(9):
            item = self.MatrixGrid.itemAt(k)
            item.widget().setButtonSymbols(2)
            item.widget().setRange(-100000.000000, 100000.000000)
            k += 1

        return self.MatrixGrid

    def changesize(self):
        if self.MatrixConstructor:
            while (self.MatrixGrid.count()):
                item = self.MatrixGrid.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

            row = self.MatrixConstructor.itemAt(1).widget().value()
            column = self.MatrixConstructor.itemAt(0).widget().value()

            for i in range(row):
                for g in range(column):
                    self.MatrixGrid.addWidget(QDoubleSpinBox(), i, g)

            for i in range(row * column):
                item = self.MatrixGrid.itemAt(i)
                item.widget().setButtonSymbols(2)
                item.widget().setRange(-100000.000000, 100000.000000)

        elif self.MatrixBase:
            while (self.MatrixGrid.count()):
                item = self.MatrixGrid.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

            row = self.MatrixBase.itemAt(1).widget().value()
            column = self.MatrixBase.itemAt(0).widget().value()

            for i in range(row):
                for g in range(column):
                    self.MatrixGrid.addWidget(QDoubleSpinBox(), i, g)

            for i in range(row * column):
                item = self.MatrixGrid.itemAt(i)
                item.widget().setButtonSymbols(2)
                item.widget().setRange(-100000.000000, 100000.000000)

            while (self.MatrixValues.count()):
                item = self.MatrixValues.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

            for i in range(row):
                self.MatrixValues.addWidget(QDoubleSpinBox())
                item = self.MatrixValues.itemAt(i)
                item.widget().setButtonSymbols(2)
                item.widget().setRange(-100000.000000, 100000.000000)

    def determinant(self):

        if self.MatrixConstructor.itemAt(1).widget().value() != self.MatrixConstructor.itemAt(0).widget().value():
            self.ErrorReport = QWidget()
            self.ErrorReport.setWindowTitle('Ошибка!')
            self.ErrorReport.resize(400, 130)
            label = QLabel('Ошибка! Число строк и столбцов\n в матрице должно совпадать', self.ErrorReport)
            label.setAlignment(Qt.AlignCenter)
            label.move(85, 60)

            frame = self.ErrorReport.frameGeometry()
            mid = QDesktopWidget().availableGeometry().center()
            frame.moveCenter(mid)
            self.ErrorReport.move(frame.topLeft())

            self.ErrorReport.show()

        else:
            MatrixData = []
            row = []
            k = 0
            for i in range(self.MatrixConstructor.itemAt(1).widget().value()):
                for g in range(self.MatrixConstructor.itemAt(0).widget().value()):
                    item = self.MatrixGrid.itemAt(k)
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

    def linEquation(self):

        if self.MatrixBase.itemAt(1).widget().value() > self.MatrixBase.itemAt(0).widget().value():
            MatrixData = []
            MatrixValueData = []
            row = []
            k = 0

            for i in range(self.MatrixBase.itemAt(1).widget().value()):
                for g in range(self.MatrixBase.itemAt(0).widget().value()):
                    item = self.MatrixGrid.itemAt(k)
                    row.append(item.widget().value())
                    k += 1
                MatrixData.append([])
                MatrixData[i].extend(row)
                row.clear()
            k = 0

            for i in range(self.MatrixValues.count()):
                item = self.MatrixValues.itemAt(i)
                MatrixValueData.append(item.widget().value())

            self.resultLinEqu = QWidget()
            self.resultLinEqu.setWindowTitle('Результаты расчетов')
            self.resultLinEqu.resize(400, 130)
            label = QLabel('x = ' + str(dot(linalg.pinv(MatrixData), MatrixValueData)), self.resultLinEqu)
            label.setAlignment(Qt.AlignCenter)
            label.move(85, 60)

            frame = self.resultLinEqu.frameGeometry()
            mid = QDesktopWidget().availableGeometry().center()
            frame.moveCenter(mid)
            self.resultLinEqu.move(frame.topLeft())

            self.resultLinEqu.show()

        elif self.MatrixBase.itemAt(1).widget().value() != self.MatrixBase.itemAt(0).widget().value():

            self.resultLinEqu = QWidget()
            self.resultLinEqu.setWindowTitle('Результаты расчетов')
            self.resultLinEqu.resize(400, 130)
            label = QLabel(('Система не имеет решений'), self.resultLinEqu)
            label.setAlignment(Qt.AlignCenter)
            label.move(85, 60)

            frame = self.resultLinEqu.frameGeometry()
            mid = QDesktopWidget().availableGeometry().center()
            frame.moveCenter(mid)
            self.resultLinEqu.move(frame.topLeft())

            self.resultLinEqu.show()

        else:
            MatrixData = []
            MatrixValueData = []
            row = []
            k = 0

            for i in range(self.MatrixBase.itemAt(1).widget().value()):
                for g in range(self.MatrixBase.itemAt(0).widget().value()):
                    item = self.MatrixGrid.itemAt(k)
                    row.append(item.widget().value())
                    k += 1
                MatrixData.append([])
                MatrixData[i].extend(row)
                row.clear()
            k = 0

            for i in range(self.MatrixValues.count()):
                item = self.MatrixValues.itemAt(i)
                MatrixValueData.append(item.widget().value())

            self.resultLinEqu = QWidget()
            self.resultLinEqu.setWindowTitle('Результаты расчетов')
            self.resultLinEqu.resize(400, 130)
            label = QLabel('x = ' + str(linalg.solve(MatrixData, MatrixValueData)), self.resultLinEqu)
            label.setAlignment(Qt.AlignCenter)
            label.move(85, 60)

            frame = self.resultLinEqu.frameGeometry()
            mid = QDesktopWidget().availableGeometry().center()
            frame.moveCenter(mid)
            self.resultLinEqu.move(frame.topLeft())

            self.resultLinEqu.show()

    def clearMatrix(self):

        row = self.MatrixGrid.rowCount()
        column = self.MatrixGrid.columnCount()

        for i in range(row * column):
            item = self.MatrixGrid.itemAt(i)
            item.widget().setValue(0.0)

        if type == 1:
            for i in range(self.MatrixValues.count()):
                item = self.MatrixValues.itemAt(i)
                item.widget().setValue(0.0)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    start = Run()

    sys.exit(app.exec_())
