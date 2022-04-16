import sys
sys.path.append('../')
from entity.Rute import Rute

class RuteManager:
    def __init__(self):
        self.rute = [] # array of rute
        self.jumlahRute = 0
        self.maxRute = 100
        print("init rute manager invoked")

    def __str__(self):
        return "RuteManager:\n" + str(self.rute) + "jumlahRute: " + str(self.jumlahRute) + "\nmaxRute: " + str(self.maxRute) + "\n"
    
    def getRute(self, index):
        return self.rute[index - 1]

    def addRute(self, idArmada, idAsal, idTujuan, waktuKeberangkatan, durasi, harga, kapasitas):
        idRute = self.jumlahRute + 1
        newRute = Rute(idRute, idArmada, idAsal, idTujuan, waktuKeberangkatan, durasi, harga, kapasitas)
        if self.jumlahRute < self.maxRute:
            self.rute.append(newRute)
            self.jumlahRute += 1
        else:
            print("Jumlah rute melebihi batas maksimal")
    
    def isRuteExist(self, idRute):
        for rute in self.rute:
            if rute.getIdRute() == idRute:
                return True
        return False

    def isRuteExistIdx(self, idRute):
        i = 0
        for rute in self.rute:
            if rute.getIdRute() == idRute:
                return i
            i += 1
        return -1

    def isRuteExist(self, idAsal, idTujuan, waktuKeberangkatan, durasi, harga, kapasitas, idArmada):
        for rute in self.rute:
            if (rute.getIdArmada() == idArmada and rute.getIdAsal == idAsal and rute.getIdTujuan == idTujuan and \
                rute.getWaktuKeberangkatan() == waktuKeberangkatan and rute.getDurasi() == durasi and rute.getHarga() == harga and \
                rute.getKapasitas() == kapasitas):
                return True
        return False

    def isRuteExistIdx(self, idAsal, idTujuan, waktuKeberangkatan, durasi, harga, kapasitas, idArmada):
        i = 0
        for rute in self.rute:
            if (rute.getIdArmada() == idArmada and rute.getIdAsal == idAsal and rute.getIdTujuan == idTujuan and \
                rute.getWaktuKeberangkatan() == waktuKeberangkatan and rute.getDurasi() == durasi and rute.getHarga() == harga and \
                rute.getKapasitas() == kapasitas):
                return i
            i += 1
        return -1

    def searchIdxRute(self, idRute):
        for i in range(len(self.rute)):
            if self.rute[i].getIdRute() == idRute:
                return i
        return -1

    def isCapacityEnough(self, requestCount, idRute):
        for rute in self.rute:
            if rute.getIdRute() == idRute:
                if requestCount < rute.getKapasitas():
                    return True
        return False