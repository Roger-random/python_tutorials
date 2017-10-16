import sys

from PyQt5.QtCore import QCoreApplication, Qt, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

def main():
  QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

  global app
  app = QGuiApplication(sys.argv)

  engine = QQmlApplicationEngine()
  engine.load(QUrl('main.qml'))
  if not engine.rootObjects():
    return -1

  app.exec_()

if __name__ == '__main__':
  main()