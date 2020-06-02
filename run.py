from PyQt5 import QtCore, QtGui, QtWidgets
import finder
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QCompleter
from PyQt5.QtCore import QSize


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(400, 350)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(30, 40, 320, 21))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(30, 142, 320, 21))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(115, 0, 151, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(100, 100, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(0, 230, 600, 16))
		self.label_3.setObjectName("label_3")
		#self.label_3.setWordWrap(True)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(110, 180, 150, 31))
		self.pushButton.setObjectName("pushButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 18))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		lineEdit = self.lineEdit
		lineEdit2 = self.lineEdit_2 

		strList = finder.return_actors()    # Create a list of words
		# We create QCompleter, in which we establish the list, and also the pointer to the parent
		completer = QCompleter(strList, lineEdit)
		completer2 = QCompleter(strList, lineEdit2)
		lineEdit.setCompleter(completer)
		lineEdit2.setCompleter(completer2)
		self.pushButton.clicked.connect(lambda: self.clicked())


	def clicked(self):
		text1, text2 =self.lineEdit.text(), self.lineEdit_2.text()
		try:
			track = finder.return_track(text1, text2)
			path = ""
			for i, t in enumerate(track):
				if(i != len(track)-1):
					path += t + " --> "
				else:
					path += t
			self.label_3.setText(path)

			self.label_3.adjustSize()
			MainWindow.resize(self.label_3.frameGeometry().width()+10, MainWindow.frameGeometry().height())
		except:
			self.label_3.setText("No connection found")



	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Actor Connector"))
		self.label.setText(_translate("MainWindow", "First Actor"))
		self.label_2.setText(_translate("MainWindow", "Second Actor"))
		self.pushButton.setText(_translate("MainWindow", "Find Connection"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
