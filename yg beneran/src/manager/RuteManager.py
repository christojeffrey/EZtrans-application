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
        return self.rute[index]

    def addRute(self, idRute, idArmada, idAsal, idTujuan, tanggalKeberangkatan, jamBerangkat, jamTiba, harga, kapasitas):
        newRute = Rute(idRute, idArmada, idAsal, idTujuan, tanggalKeberangkatan, jamBerangkat, jamTiba, harga, kapasitas)
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