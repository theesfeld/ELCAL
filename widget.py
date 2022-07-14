#!/usr/bin/python

import sys
from PySide6.QtWidgets import (QLabel, QSpinBox, QComboBox, QPushButton, QApplication,
                               QVBoxLayout, QDialog)

capacityFactor = {
            'Office (Single Tenant)': .33,
            'Office (Multi Tenant)': .22,
            'Residential': .17,
            'Hotel': .38,
            'Hospital': .12
        }

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.areaPerFloorLabel = QLabel('Average Area Per Floor')
        self.areaPerFloor = QSpinBox()
        self.areaPerFloor.setMaximum(4000)
        self.buildingFloorsLabel = QLabel('Floors in Building')
        self.buildingFloors = QSpinBox()
        self.buildingFloors.setMaximum(100)
        self.buildingTypeLabel = QLabel('Building Type')
        self.buildingType = QComboBox()
        self.buildingType.clear()

        for text, cf in capacityFactor.items():
            self.buildingType.addItem(text)
        
        self.peoplePerCarLabel = QLabel('People Per Car')
        self.peoplePerCar = QSpinBox()
        self.estimateButton = QPushButton('Estimate')
        self.outputLabel = QLabel('')
        self.estimateButton.clicked.connect(self.estimate)

        vbox = QVBoxLayout()
        vbox.addWidget(self.areaPerFloorLabel)
        vbox.addWidget(self.areaPerFloor)
        vbox.addWidget(self.buildingFloorsLabel)
        vbox.addWidget(self.buildingFloors)
        vbox.addWidget(self.buildingTypeLabel)
        vbox.addWidget(self.buildingType)
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
        A = self.areaPerFloor.value()
        F = self.buildingFloors.value()
        C = capacityFactor.get(self.buildingType.currentText())
        E = self.peoplePerCar.value() * .18
        N = (A*F*C)/(226*E)
        self.outputLabel.setText(f'{round(N)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
