import sys
sys.path.append('../')
from entity.Tiket import Tiket

class TiketManager:
    def __init__(self):
        print("init tiket manager invoked")
        # array of tiket
        self.tiket = []
    def addTiket(self, idTiket, idPenumpang, username, idRute, status, namaPenumpang, tanggalPemesanan):
        tiket = Tiket(idTiket, idPenumpang, username, idRute, status, namaPenumpang, tanggalPemesanan)
        self.tiket.append(tiket)
    def isTiketExist(self, idTiket):
        for tiket in self.tiket:
            if tiket.getIdTiket() == idTiket:
                return True
        return False
    
