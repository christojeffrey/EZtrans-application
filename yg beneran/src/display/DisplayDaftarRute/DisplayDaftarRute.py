from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication

Widget, Window = uic.loadUiType("DisplayDaftarRute.ui")

import sys
sys.path.append('../../')
from manager.RuteManager import RuteManager

class DisplayDaftarRute:
    def __init__(self, ruteManager):
        self.rutes = ruteManager.rute
        self.app = QApplication([])
        self.window = Window()
        self.widget = Widget()

    def show(self):
        self.window.show()
        self.app.exec()
        self.loadData()
        
    def loadData(self):
        row = 0
        self.tableRute.setRowCount(self.rutes.jumlahRute)
        for rute in self.rutes:
            self.tableRute.setItem(row, 0, QtWidgets.QTableWidgetItem(rute.getIdRute()))
            self.tableRute.setItem(row, 1, QtWidgets.QTableWidgetItem(rute.getIdArmada()))
            self.tableRute.setItem(row, 2, QtWidgets.QTableWidgetItem(rute.getLokasiAwal()))
            self.tableRute.setItem(row, 3, QtWidgets.QTableWidgetItem(rute.getLokasiAkhir()))
            self.tableRute.setItem(row, 4, QtWidgets.QTableWidgetItem(rute.getHarga()))
            self.tableRute.setItem(row, 5, QtWidgets.QTableWidgetItem(rute.getDurasi()))
            self.tableRute.setItem(row, 6, QtWidgets.QTableWidgetItem(rute.getWaktuKeberangkatan()))
            self.tableRute.setItem(row, 6, QtWidgets.QTableWidgetItem(rute.getKapasitasTotal()))
            row += 1

# lokasiAwal, lokasiAkhir, harga, durasi, waktuKeberangkatan, kapasitasTotal, idBus = FormTambahRute().show()
# print (lokasiAwal, lokasiAkhir, harga, durasi, waktuKeberangkatan, kapasitasTotal, idBus)
newRuteMng = RuteManager()
newRuteMng.addRute(1, 2, 3, '5', 20, 15, 10)
DisplayDaftarRute(newRuteMng).show()