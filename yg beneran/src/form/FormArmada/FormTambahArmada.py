from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# directorynya harus digituin, soalnya yg manggil itu main :(
Form, Window = uic.loadUiType("form/FormArmada/FormTambahArmada.ui")


class FormTambahArmada:
    def __init__(self):
        self.currentIdArmada = ""
        self.currentNama = ""
        self.currentKapasitas = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

    def show(self, errorMessage):
        # bind
        self.form.ArmadaButton.clicked.connect(self.TambahArmadaButtonClicked)
        self.form.errorMessageLabel.setText(errorMessage)
        # show
        self.window.show()
        self.app.exec()
        return self.currentIdArmada, self.currentNama, self.currentKapasitas

    def TambahArmadaButtonClicked(self):
        self.currentIdArmada = self.form.IdcurrentIdArmadaLineEdit.text()
        self.currentNama = self.form.NamaLineEdit.text()
        self.currentKapasitas = self.form.NamaLineEdit.text()
        self.window.close()
        print("Tambah armada Button Clicked")
