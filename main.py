import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QLineEdit,QFileDialog,QHBoxLayout


class pencere(QWidget):

def __init__(self):
		super().__init__()
		self.init_ui()

def init_ui(self):
		self.yazi_alani = QTextEdit()
		self.temizle = QPushButton("temizle")
		self.ac = QPushButton("aç")
		self.kaydet = QPushButton("kaydet")

    hbox = QHBoxLayout()
		vbox = QVBoxLayout()
		hbox.addWidget(self.temizle)
		hbox.addWidget(self.ac)
		hbox.addWidget(self.kaydet)
		vbox.addWidget(self.yazi_alani)
		vbox.addLayout(hbox)
		
    self.setLayout(vbox)
		self.temizle.clicked.connect(self.yaziyi_temizle)
		self.ac.clicked.connect(self.dosya_ac)
		self.kaydet.clicked.connect(self.dosya_kaydet)
		self.setGeometry(300,100,500,500)
		self.show()
	
  def yaziyi_temizle(self):
		self.yazi_alani.clear()
	
  def dosya_ac(self):
		dosya_ismi = QFileDialog.getOpenFileName(self,"dosya aç",os.getenv("HOME"))
		with open(dosya_ismi[0],"r") as file:
			self.yazi_alani.setText(file.read())
	
  def dosya_kaydet(self):
		dosya_ismi = QFileDialog.getSaveFileName(self,"dosya kaydet",os.getenv("HOME"))
		with open(dosya_ismi[0] , "w") as file:
			file.write(self.yazi_alani.toPlainText())


app = QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())



