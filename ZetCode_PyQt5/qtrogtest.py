import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
  
  def __init__(self):
    super().__init__()
    self.initUI()
    
  def initUI(self):
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
