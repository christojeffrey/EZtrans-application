import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# directorynya harus digituin, soalnya yg manggil itu main :(
Form, Window = uic.loadUiType("form/FormMasukanPenumpang/FormMasukanPenumpang.ui")

class MasukanPenumpang():
    def __init__(self):
        self.namaPenumpang = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
    def show(self, errorMessage):
        #bind
        self.form.tambahPenumpangButton.clicked.connect(self.tambahPenumpangButtonClicked)
        self.form.pesanButton.clicked.connect(self.pesanButtonClicked)
        self.form.errorMessageLabel.setText(errorMessage)
        # show
        self.window.show()
        self.app.exec()
        return self.namapenumpang
    def tambahPenumpangButtonClicked(self):
        self.namaPenumpang = self.form.usernameLineEdit.text()
        print("Penumpang Berhasil Ditambahkan")
    def pesanButtonClicked(self):
        self.window.close()
        print("Data Tiket Ditambahkan")

