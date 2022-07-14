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
        self.elevatorTableLabel = QLabel('Elevator Capacity (lb)')
        self.estimateButton = QPushButton('Estimate')
        self.outputLabel = QLabel()
        self.outputLabel.clear()
        self.estimateButton.clicked.connect(self.estimate)
        self.elevatorTable = QTableWidget(30,6)
        self.elevatorTable.setHorizontalHeaderLabels(['Capacity', 'Speed', 'Acceleration', 'Jerk', 'Door Open', 'Door Close'])
        self.riserTable = QTableWidget(80,3)
        self.riserTable.setHorizontalHeaderLabels(['Floor', 'Height', 'Population'])

        grid = QGridLayout()
        grid.addWidget(self.elevatorTableLabel,3,1)
        grid.addWidget(self.elevatorTable,0,0,5,1)
        grid.addWidget(self.riserTable,0,1,5,1)
        
        grid.addWidget(self.capacityFactorLabel,2,1)
        grid.addWidget(self.capacityFactor,2,2)
        grid.addWidget(self.estimateButton,5,1)
        grid.addWidget(self.outputLabel,5,2)
        grid.rowStretch(1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 900)
        self.setWindowTitle('Elevator Approximator')
        self.show()

    def estimate(self):
        cf = self.capacityFactor.value()
        cc = self.elevatorCapacity.value()
        ui = []
        j = 
        n = []
        # ElevatorVariables.md has variable list
        
        # persons per elevator
        # p=\left(\frac{cf}{100}\right)\cdot{cc}
        p = (cf/100) * cc
        
        # Effective Building population
        # Ueff = 0
        # for floorpopulation in list of floors/populations
        #   ueff = ueff + i

        # Average Highest Reversal Floor 
        # H=\sum_{j=1}^{N-1}\left(\sum_{i=1}^{j}\frac{U_i}{U_eff}\right)^P
        h = sum(sum(ui/((ueff)), (i, 1, j))**p, (j, 1, n - 1))

        # Average Number Of Stops Made During Round Trip
        # S=N-\sum_{i=1}^{N}\left(1-\frac{U_i}{U_eff}\right)^P
        s = n - sum((-ui/(ueff) + 1)**p, (i, 1, n))

        # Average Time For Passenger To Load And Unload The Elevator
        # tp=\frac{({tl}+{tu})}{2}
        tp = (tl+tu)/2

        # Time taken for the lift to travel between two adjacent floors at rated speed
        # tv=\frac{df}{v}
        tv = df / v

        # cycle time (travel to floor, open / close doors)
        # t={tfl}+{tc}+{to}
        t = tfl + tc + to

        # time consumed making a single stop
        # ts={t}-{tv}
        ts = t - tv

        # Round Trip Time (RTT)
        # rtt=\left[\right]
        rtt = (2*h*tv) + ((s + 1)*ts) + (2*p*tp)

        # Up Peak Round Trip Time (UPPRTT) [RTT with 'losses']
        # uppint=\frac{rtt}{l}
        uppint = rtt/l

        # Up Peak Handling Capacity (UPPHC)
        # NUMBER of people moved in 5 minutes
        # upphc=\frac{300\cdot{p}\cdot{*}l}{rtt}   
        upphc = 300*p*l/rtt

        # Handling Capacity
        # PERCENT of people moved in 5 minutes
        # hc=\frac{{upphc}\cdot{100}}{ueff}
        hc = (upphc*100)/ueff

        print(f'Calculating')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
