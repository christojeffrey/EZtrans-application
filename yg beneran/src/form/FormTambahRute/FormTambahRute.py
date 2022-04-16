from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox

Form, Window = uic.loadUiType("form/FormTambahRute/FormTambahRute.ui")

class FormTambahRute:
    def __init__(self):
        self.lokasiAwal = ""
        self.lokasiAkhir = ""
        self.harga = ""
        self.durasi = ""
        self.waktuKeberangkatan = ""
        self.kapasitasTotal = ""
        self.idBus = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

    def show(self):
        #bind
        self.form.addRuteBt.clicked.connect(self.addRuteButtonClicked)
        # show
        self.window.show()
        self.app.exec()

        if (self.lokasiAwal == "" or self.lokasiAkhir == "" or self.harga == "" or self.durasi == "" or self.waktuKeberangkatan == "" or self.kapasitasTotal == "" or self.idBus == ""):
            self.showErrorDialog()
        else:
            return self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.waktuKeberangkatan, self.kapasitasTotal, self.idBus
        
    def addRuteButtonClicked(self):
        self.lokasiAwal = self.form.lokasiAwal.text()
        self.lokasiAkhir = self.form.lokasiAkhir.text()
        self.harga = self.form.harga.text()
        self.durasi = self.form.harga.text()
        self.waktuKeberangkatan = self.form.waktuKeberangkatan.text()
        self.kapasitasTotal = self.form.kapasitasTotal.text()
        self.idBus = self.form.idBus.text()
        self.window.close()
        
        print("Tambah Rute Button Clicked")

    def showErrorDialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Masukkan nilai pada kolom yang tersedia!")
        msg.exec()
        FormTambahRute().show()

# lokasiAwal, lokasiAkhir, harga, durasi, waktuKeberangkatan, kapasitasTotal, idBus = FormTambahRute().show()
# print (lokasiAwal, lokasiAkhir, harga, durasi, waktuKeberangkatan, kapasitasTotal, idBus)