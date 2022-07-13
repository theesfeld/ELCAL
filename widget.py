#!/usr/bin/python

import sys
from PySide6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        areaPerFloorLabel = QtWidgets.QLabel('Average Area Per Floor')
        areaPerFloor = QtWidgets.QSpinBox()
        buildingFloorsLabel = QtWidgets.QLabel('Floors in Building')
        buildingFloors = QtWidgets.QSpinBox()
        buildingTypeLabel = QtWidgets.QLabel('Building Type')
        buildingType = QtWidgets.QComboBox()
        estimateButton = QtWidgets.QPushButton('Estimate')
        estimateButton.clicked.connect(self.estimate)
        outputLabel = QtWidgets.QLabel()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(areaPerFloorLabel)
        vbox.addWidget(areaPerFloor)
        vbox.addWidget(buildingFloorsLabel)
        vbox.addWidget(buildingFloors)
        vbox.addWidget(buildingTypeLabel)
        vbox.addWidget(buildingType)
        vbox.addWidget(estimateButton)
        vbox.addWidget(outputLabel)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Elevator Approximator')
        self.show()

        def estimate(self):

            # N = (A*F*C)/(226*E)
        
            self.outputLabel.setText('test')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
