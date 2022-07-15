from os import lseek
import sys
from xmlrpc.client import GzipDecodedResponse
from PySide6.QtWidgets import (QLabel, QSpinBox, QPushButton, QApplication,
                               QGridLayout, QDialog, QTableWidget)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.elevator = self.Elevator()
        self.building = self.Building()

        self.elevatorNumberLabel = QLabel('Number of Elevators')
        self.elevatorNumber = QSpinBox()
        self.elevatorCapacityFactorLabel = QLabel('Capacity Factor (%)')
        self.elevatorCapacityFactor = QSpinBox()
        self.elevatorCapacityFactor.setMaximum(100)
        self.elevatorCapacityLabel = QLabel('Elevator Capacity (lb)')
        self.elevatorCapacity = QSpinBox()
        self.elevatorCapacity.setMaximum(20000)
        self.elevatorDoorOLabel = QLabel('Door Open Time (s)')
        self.elevatorDoorO = QSpinBox()
        self.elevatorDoorCLabel = QLabel('Door Close Time (s)')
        self.elevatorDoorC = QSpinBox()
        self.elevatorSpeedLabel = QLabel('Elevator Contract Speed (m/s)')
        self.elevatorSpeed = QSpinBox()
        self.elevatorAccelLabel = QLabel('Acceleration (m/s/2)')
        self.elevatorAccel = QSpinBox()
        self.elevatorJerkLabel = QLabel('Jerk (m/s/3)')
        self.elevatorJerk = QSpinBox()
        self.buildingFloorsLabel = QLabel('Building Floors')
        self.buildingFloors = QSpinBox()
        self.buildingPopulationLabel = QLabel('Building Population')
        self.buildingPopulation = QSpinBox()
        self.buildingPassengerLULabel = QLabel('Loading / Unloading Time (s)')
        self.buildingPassengerLU = QSpinBox()
        self.estimateButton = QPushButton('Calculate')
        self.estimateButton.clicked.connect(self.calculate)
        self.outputLabel = QLabel()
        self.outputLabel.clear()

        grid = QGridLayout()
        grid.addWidget(self.elevatorNumberLabel,0,0)
        grid.addWidget(self.elevatorNumber,0,1)
        grid.addWidget(self.elevatorSpeedLabel,1,0)
        grid.addWidget(self.elevatorSpeed,1,1)
        grid.addWidget(self.elevatorAccelLabel,2,0)
        grid.addWidget(self.elevatorAccel,2,1)
        grid.addWidget(self.elevatorJerkLabel,3,0)
        grid.addWidget(self.elevatorJerk,3,1)
        grid.addWidget(self.elevatorCapacityLabel,4,0)
        grid.addWidget(self.elevatorCapacity,4,1)
        grid.addWidget(self.elevatorCapacityFactorLabel,5,0)
        grid.addWidget(self.elevatorCapacityFactor,5,1)
        grid.addWidget(self.elevatorDoorOLabel,6,0)
        grid.addWidget(self.elevatorDoorO,6,1)
        grid.addWidget(self.elevatorDoorCLabel,7,0)
        grid.addWidget(self.elevatorDoorC,7,1)
        grid.addWidget(self.buildingFloorsLabel,8,0)
        grid.addWidget(self.buildingFloors,8,1)
        grid.addWidget(self.buildingPopulationLabel,9,0)
        grid.addWidget(self.buildingPopulation,9,1)
        grid.addWidget(self.buildingPassengerLULabel,10,0)
        grid.addWidget(self.buildingPassengerLU,10,1)
        grid.addWidget(self.outputLabel,11,0)
        grid.addWidget(self.estimateButton,11,1)
        grid.setVerticalSpacing(-5)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 900)
        self.setWindowTitle('Elevator Up Peak Calculator')
        self.show()

    class Building():
        def __init__(self):
            floors = 0
            population = 0

    class Elevator():
        def __init__(self):
            capacity = 0
            capacityFactor = 0
            doorOpenTime = 0
            doorCloseTime = 0
            passengerLoading = 0
            passengerUnloading = 0
            speed = 0
            jerk = 0
            acceleration = 0

    def calculate(self):
        elevators = []

        cf = self.elevatorCapacityFactor.value()
        cc = self.elevatorCapacity.value()
        n = self.elevatorNumber.value()
        tl = tu = self.buildingPassengerLU.value()
        j = self.elevatorJerk.value() 
        v = self.elevatorSpeed.value()
        to = self.elevatorDoorO.value()
        tc = self.elevatorDoorC.value()
        # ElevatorVariables.md has variable list
        
        # persons per elevator
        # p=\left(\frac{cf}{100}\right)\cdot{cc}
        p = (cf/100) * cc
        
        # Effective Building population
        # Ueff = 0
        # for floorpopulation in list of floors/populations
        #   ueff = ueff + i
        ueff = self.buildingPopulation.value()

        # Average Highest Reversal Floor 
        # H=\sum_{j=1}^{N-1}\left(\sum_{i=1}^{j}\frac{U_i}{U_eff}\right)^P
        #h = sum(sum(ui/((ueff)), (i, 1, j))**p, (j, 1, n - 1))

        # Average Number Of Stops Made During Round Trip
        # S=N-\sum_{i=1}^{N}\left(1-\frac{U_i}{U_eff}\right)^P
        #s = n - sum((-ui/(ueff) + 1)**p, (i, 1, n))

        # Average Time For Passenger To Load And Unload The Elevator
        # tp=\frac{({tl}+{tu})}{2}
        tp = (tl+tu)/2

        # Time taken for the lift to travel between two adjacent floors at rated speed
        # tv=\frac{df}{v}
        #tv = df / v

        # cycle time (travel to floor, open / close doors)
        # t={tfl}+{tc}+{to}
        #t = tfl + tc + to

        # time consumed making a single stop
        # ts={t}-{tv}
        #ts = t - tv

        # Round Trip Time (RTT)
        # rtt=\left[\right]
        #rtt = (2*h*tv) + ((s + 1)*ts) + (2*p*tp)

        # Up Peak Round Trip Time (UPPRTT) [RTT with 'losses']
        # uppint=\frac{rtt}{l}
        #uppint = rtt/l

        # Up Peak Handling Capacity (UPPHC)
        # NUMBER of people moved in 5 minutes
        # upphc=\frac{300\cdot{p}\cdot{*}l}{rtt}   
        #upphc = 300*p*l/rtt

        # Handling Capacity
        # PERCENT of people moved in 5 minutes
        # hc=\frac{{upphc}\cdot{100}}{ueff}
        #hc = (upphc*100)/ueff

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
