import sys
sys.path.append('../')
from form.FormTambahRute.FormTambahRute import FormTambahRute
from manager.RuteManager import RuteManager

class TambahRuteController:
    def __init__(self, ruteManager):
        print("init Tambah Rute Controller invoked")
        self.lokasiAwal = ""
        self.lokasiAkhir = ""
        self.harga = 0
        self.durasi = 0 # dalam menit
        self.waktuKeberangkatan = ""
        self.kapasitasTotal = 0
        self.idBus = 0
        self.display = FormTambahRute()
        self.rutes = ruteManager
    
    def initiate(self):
        print("inititate Tambah Rute Controller invoked")
        while (True):
            self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.waktuKeberangkatan, self.kapasitasTotal, self.idBus = self.display.show()
            idPilihanRute = self.rutes.isRuteExistIdx(self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.waktuKeberangkatan, self.kapasitasTotal, self.idBus)
            if (idPilihanRute != -1):
                choice = str(input('Rute yang hendak ditambahkan sudah ada. (Ubah/Tambah) '))
                if (choice == "Ubah"):
                    self.rutes.getRute(idPilihanRute).setLokasiAwal(self.lokasiAwal)
                    self.rutes.getRute(idPilihanRute).setLokasiAkhir(self.lokasiAkhir)
                    self.rutes.getRute(idPilihanRute).setWaktuKeberangkatan(self.waktuKeberangkatan)
                    self.rutes.getRute(idPilihanRute).setDurasi(self.durasi)
                    self.rutes.getRute(idPilihanRute).setHarga(self.harga)
                    self.rutes.getRute(idPilihanRute).setKapasitas(self.kapasitasTotal)
                    self.rutes.getRute(idPilihanRute).setIdArmada(self.idBus)
                    break
                elif (choice == "Tambah"):
                    self.rutes.addRute(self.idBus, self.lokasiAwal, self.lokasiAkhir, self.waktuKeberangkatan, self.durasi, self.harga, self.kapasitasTotal)
                    break
                else:
                    print("Command tidak valid!")
                break
            else:
                self.rutes.addRute(self.idBus, self.lokasiAwal, self.lokasiAkhir, self.waktuKeberangkatan, self.durasi, self.harga, self.kapasitasTotal)
                break
        return self.lokasiAwal, self.lokasiAkhir, self.harga, self.durasi, self.waktuKeberangkatan, self.kapasitasTotal, self.idBus