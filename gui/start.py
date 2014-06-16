import sys
import re
from PyQt4 import QtCore, QtGui
from puzz import Ui_puzzle

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_puzzle()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.button_go,QtCore.SIGNAL('clicked()'), self.search_pattern)

	def search_pattern(self):
		lis = []
		pattern = str(self.ui.text_pattern.text())
		length = len(pattern)
		pattern = pattern.replace('?','\w')		
		words = open('/usr/share/dict/words','r')
		for word in words:
			if len(word)== int(length)+1 and re.search(pattern,word):
				lis.append(word)
		
		txt = ''
		for w in lis: txt += w
		self.ui.text_result.setText(txt)
		self.ui.statusbar.showMessage("%d words found" % len(lis))
				

	

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())


