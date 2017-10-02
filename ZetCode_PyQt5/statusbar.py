import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
  
  def __init__(self):
    super().__init__()
    
    self.initUI()
    
  def initUI(self):
    self.statusBar().showMessage('Ready Status Message')
    
    self.setGeometry(300, 380, 800, 480)
    self.setWindowTitle('Demo for statusBar')
    self.show()
    
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
