#!/usr/bin/python

import sys
from PySide6.QtWidgets import (QLabel, QSpinBox, QComboBox, QPushButton, QApplication,
                               QVBoxLayout, QDialog)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.areaPerFloorLabel = QLabel('Average Area Per Floor')
        self.areaPerFloor = QSpinBox()
        self.areaPerFloor.setMaximum(4000)
        self.buildingFloorsLabel = QLabel('Floors in Building')
        self.buildingFloors = QSpinBox()
        self.buildingFloors.setMaximum(100)
        self.capacityFactorLabel = QLabel('Capacity Factor')
        self.capacityFactor = QSpinBox()
        self.capacityFactor.setMaximum(100)
        self.elevatorCapacityLabel = QLabel('Elevator Capacity')
        self.elevatorCapactiy = QSpinBox()
        self.elevatorCapacity.setMaximum(100)
        self.estimateButton = QPushButton('Estimate')
        self.outputLabel = QLabel('')
        self.estimateButton.clicked.connect(self.estimate)

        vbox = QVBoxLayout()
        vbox.addWidget(self.areaPerFloorLabel)
        vbox.addWidget(self.areaPerFloor)
        vbox.addWidget(self.buildingFloorsLabel)
        vbox.addWidget(self.buildingFloors)
        vbox.addWidget(self.capacityFactorLabel)
        vbox.addWidget(self.capacityFactor)
        vbox.addWidget(self.peoplePerCarLabel)
        vbox.addWidget(self.peoplePerCar)
        vbox.addWidget(self.estimateButton)
        vbox.addWidget(self.outputLabel)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Elevator Approximator')
        self.show()

    def estimate(self):
        A = self.areaPerFloor.value()*10.764
        F = self.buildingFloors.value()
        C = self.capacityFactor.value()/100
        E = (self.elevatorCapacity.value * C) / 165
        N = (A*F*C)/(226*E)
        self.outputLabel.setText(f'{round(N)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
