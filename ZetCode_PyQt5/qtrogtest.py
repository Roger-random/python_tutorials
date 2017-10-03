import sys
from collections import OrderedDict
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget

class Relay(QLabel):
  
  relayEnergized = False
  
  def __init__(self, name, energized = False):
    super().__init__(name)
    if(energized):
      self.energize()
    else:
      self.deenergize()    
    
  def energize(self):
    self.relayEnergized = True
    self.setStyleSheet("QLabel {background-color : green; color : white}")
    
  def deenergize(self):
    self.relayEnergized = False
    self.setStyleSheet("QLabel {background-color : white; color : gray}")
    

class MainWindow(QMainWindow):
  
  global relays
  relays = OrderedDict()
  
  def __init__(self):
    super().__init__()
    self.createRelays()
    self.initUI()
    
  def createRelays(self):
    relays["Main"] = Relay("Main 220V")
    relays["VacPump"] = Relay("Vacuum Pump")
    relays["Heater"] = Relay("Heat")
    relays["VacValve"] = Relay("Table Vacuum")
    relays["UpValve"] = Relay("Up")
    relays["DownValve"] = Relay("Down")
    relays["HeaterFwd"] = Relay("Forward")
    relays["BlowOffValve"] = Relay("Table Air")
    relays["CoverMag"] = Relay("Magnet")
    
  def initUI(self):
    for v in relays.values():
      self.statusBar().addPermanentWidget(v)
    self.setGeometry(0, 0, 800, 480)
    self.setWindowTitle("Roger's Qt Tests")
    self.show()

def main():
  global app
  app = QApplication(sys.argv)
  
  mw = MainWindow()
  
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
