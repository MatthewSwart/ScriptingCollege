import sys
from PyQt4 import QtCore, QtGui
from hello_ui import Ui_MainWindow

class Hello(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Hello()
	myapp.show()
	sys.exit(app.exec_())
