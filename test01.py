import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, \
    qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      exitAction = QAction(QIcon('exit.png'), 'Exit', self)
      exitAction.setShortcut('Ctrl+Q')
      exitAction.setStatusTip('Exit application')
      exitAction.triggered.connect(qApp.quit)

      QToolTip.setFont(QFont('SansSerif', 10))
      self.setToolTip('This is a <b>QWidget</b> widget')
      self.statusBar().showMessage('Far From Home')

      menubar = self.menuBar()
      menubar.setNativeMenuBar(False)
      filemenu = menubar.addMenu('&File')
      filemenu.addAction(exitAction)

      btn = QPushButton('Button', self)
      btn.setToolTip('<b>Nuclear Launch<b> Button')
      btn.move(250,250)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)

      btn = QPushButton('Quit', self)
      btn.setToolTip('<b>Far From Home<b>')
      btn.move(480,350)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)

      self.toolbar = self.addToolBar('Exit')
      self.toolbar.addAction(exitAction)

      self.setWindowTitle('Centering')
      self.setWindowIcon(QIcon('web.png'))
      self.resize(600, 400)
      self.center()
      self.show()

  def center(self):
      qr = self.frameGeometry()
      cp = QDesktopWidget().availableGeometry().center()
      qr.moveCenter(cp)
      self.move(qr.topLeft())


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())