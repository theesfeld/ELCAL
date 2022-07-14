from os import lseek
import sys
from PySide6.QtWidgets import (QLabel, QSpinBox, QPushButton, QApplication,
                               QGridLayout, QDialog, QTableWidget)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.capacityFactorLabel = QLabel('Capacity Factor (%)')
        self.capacityFactor = QSpinBox()
        self.capacityFactor.setMaximum(100)
        self.elevatorCapacityLabel = QLabel('Elevator Capacity (lb)')
        self.elevatorCapacity = QSpinBox()
        self.elevatorCapacity.setMaximum(20000)
        self.estimateButton = QPushButton('Estimate')
        self.outputLabel = QLabel()
        self.outputLabel.clear()
        self.estimateButton.clicked.connect(self.estimate)
        self.riserTable = QTableWidget(80,3)
        self.riserTable.setHorizontalHeaderLabels(['Floor', 'Height', 'Population'])

        grid = QGridLayout()
        grid.addWidget(self.capacityFactorLabel,2,1)
        grid.addWidget(self.capacityFactor,2,2)
        grid.addWidget(self.elevatorCapacityLabel,3,1)
        grid.addWidget(self.elevatorCapacity,3,2)
        grid.addWidget(self.riserTable,0,0,5,1)
        grid.addWidget(self.estimateButton,5,1)
        grid.addWidget(self.outputLabel,5,2)
        grid.rowStretch(1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 900)
        self.setWindowTitle('Elevator Approximator')
        self.show()

    def estimate(self):

        # ElevatorVariables.md has variable list
        
        # persons per elevator
        # P = (CF/100) * CC
        
        # Effective Building population
        # Ueff = 0
        # for floorpopulation in list of floors/populations
        #   ueff = ueff + i

        # Average Highest Reversal Floor
        # H = 

        # Average Number Of Stops Made During Round Trip
        # S = 

        # Average Time For Passenger To Load And Unload The Elevator
        # tp = (tl+tu)/2

        # Time taken for the lift to travel between two adjacent floors at rated speed
        # tv = df / v

        # cycle time (travel to floor, open / close doors)
        # T = tfl + tc + to

        # time consumed making a single stop
        # ts = T - tv

        # Round Trip Time (RTT)
        # RTT = (2*H*tv) + ((S + 1)*ts) + (2*P*tp)

        # Up Peak Round Trip Time (UPPRTT) [RTT with 'losses']
        # UPPINT = RTT/L

        # Up Peak Handling Capacity (UPPHC)
        # NUMBER of people moved in 5 minutes
        # UPPHC = (300*(P*L))/RTT

        # Handling Capacity
        # PERCENT of people moved in 5 minutes
        # HC = (UPPHC*100)/ueff

        #A = self.areaPerFloor.value()*10.764
        #F = self.buildingFloors.value()
        #C = float((self.capacityFactor.value()/100))
        #E = (self.elevatorCapacity.value()*C) / 165
        #N = (A*F*C)/(226*E)
        #self.outputLabel.setText(f'{round(N)}')
        print(f'Calculating')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
