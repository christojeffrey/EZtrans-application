from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QComboBox

# Form, Window = uic.loadUiType("form/FormUbahRute/FormUbahRute.ui")
Form, Window = uic.loadUiType("FormUbahRute.ui")

class FormUbahRute:
    def __init__(self, choices):
        self.pilihan = choices # array of pilihan rute yang dapat diubah
        self.pilihanRute = 0
        self.lokasiAwal = ""
        self.lokasiAkhir = ""
        self.harga = 0
        self.durasi = 0 # dalam menit
        self.jamKeberangkatan = ""
        self.kapasitasTotal = 0
        self.idBus = 0

        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.form.comboBox.addItems(choices)
        self.form.comboBox.currentIndexChanged.connect(self.selectionChanged)

    def show(self):
        #bind
        self.form.addRuteBt.clicked.connect(self.addRuteButtonClicked)
        # show
        self.window.show()
        self.app.exec()

        if (self.lokasiAwal == "" or self.lokasiAkhir == "" or self.harga == "" or self.durasi == "" or self.jamKeberangkatan == "" or self.kapasitasTotal == "" or self.idBus == ""):
            self.showErrorDialog()
        else:
            return self.pilihanRute, self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.jamKeberangkatan, self.kapasitasTotal, self.idBus
        
    def addRuteButtonClicked(self):
        self.pilihanRute = int(self.form.comboBox.currentText())
        self.lokasiAwal = self.form.lokasiAwal.text()
        self.lokasiAkhir = self.form.lokasiAkhir.text()
        self.harga = int(self.form.harga.text())
        self.durasi = int(self.form.harga.text())
        self.jamKeberangkatan = self.form.jamKeberangkatan.text()
        self.kapasitasTotal = int(self.form.kapasitasTotal.text())
        self.idBus = int(self.form.idBus.text())
        self.window.close()
        
        print("Ubah Rute Button Clicked")

    def showErrorDialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Masukkan nilai pada kolom yang tersedia!")
        msg.exec()
        FormUbahRute().show()
    
    def selectionChanged(self):
        print (self.cb.currentText(), "selected")

# pilihanRute, lokasiAwal, lokasiAkhir, harga, durasi, jamKeberangkatan, kapasitasTotal, idBus = FormUbahRute(['1','2']).show()
# print (pilihanRute, lokasiAwal, lokasiAkhir, harga, durasi, jamKeberangkatan, kapasitasTotal, idBus)