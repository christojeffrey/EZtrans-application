#lokasiAwal, lokasiAkhir, harga, durasi, jamKeberangkatan, kapasitasTotal, idBus = FormTambahRute().show()
import sys
sys.path.append('../')
from form.FormUbahRute.FormUbahRute import FormUbahRute
from manager.RuteManager import RuteManager

class UbahRuteController:
    def __init__(self):
        print("init Ubah Rute Controller invoked")
        self.pilihanRute = 0
        self.lokasiAwal = ""
        self.lokasiAkhir = ""
        self.harga = 0
        self.durasi = 0 # dalam menit
        self.tanggalKeberangkatan = ""
        self.jamKeberangkatan = ""
        self.kapasitasTotal = 0
        self.idBus = 0
        self.display = FormUbahRute()
        self.rutes = RuteManager()
    
    def initiate(self):
        print("inititate Ubah Rute Controller invoked")
        while (True):
            self.pilihanRute, self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.jamKeberangkatan, self.kapasitasTotal, self.idBus = self.display.show()
            if (self.rutes.isRuteExist(self.pilihanRute)):
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setLokasiAwal(self.getLokasiAwal())
                break
            else:
                self.rutes.addRute(self.pilihanRute, self.idBus, self.lokasiAwal, self.lokasiAkhir, self.tanggalKeberangkatan, self.jamKeberangkatan, self.durasi, self.harga, self.kapasitasTotal)
                break
        return self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.tanggalKeberangkatan, self.jamKeberangkatan, self.kapasitasTotal, self.idBus