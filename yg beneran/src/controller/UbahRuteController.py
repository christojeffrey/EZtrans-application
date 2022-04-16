#lokasiAwal, lokasiAkhir, harga, durasi, jamKeberangkatan, kapasitasTotal, idBus = FormTambahRute().show()
import sys
sys.path.append('../')
from form.FormUbahRute.FormUbahRute import FormUbahRute
from manager.RuteManager import RuteManager

class UbahRuteController:
    def __init__(self, ruteManager):
        print("init Ubah Rute Controller invoked")
        self.pilihanRute = 0
        self.lokasiAwal = ""
        self.lokasiAkhir = ""
        self.harga = 0
        self.durasi = 0 # dalam menit
        self.waktuKeberangkatan = ""
        self.kapasitasTotal = 0
        self.idBus = 0
        self.display = FormUbahRute()
        self.rutes = ruteManager
    
    def initiate(self):
        print("inititate Ubah Rute Controller invoked")
        while (True):
            self.pilihanRute, self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.waktuKeberangkatan, self.kapasitasTotal, self.idBus = self.display.show()
            if (self.rutes.isRuteExist(self.pilihanRute)):
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setLokasiAwal(self.lokasiAwal)
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setLokasiAkhir(self.lokasiAkhir)
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setWaktuKeberangkatan(self.waktuKeberangkatan)
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setDurasi(self.durasi)
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setHarga(self.harga)
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setKapasitas(self.kapasitasTotal)
                self.rutes.getRute(self.searchIdxRute(self.pilihanRute)).setIdArmada(self.idBus)
                break
            else:
                print('Rute yang dicari tidak ditemukan. Ditambahkan rute baru!')
                self.rutes.addRute(self.idBus, self.lokasiAwal, self.lokasiAkhir, self.waktuKeberangkatan, self.durasi, self.harga, self.kapasitasTotal)
                break
        return self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.waktuKeberangkatan, self.kapasitasTotal, self.idBus