from entity.Armada import Armada
import sys
sys.path.append('../')


class ArmadaManager:
    def __init__(self):
        print("init armada manager invoked")
        # array of armada
        self.armada = []

    def addArmada(self, IdArmada, nama, kapasitas):
        armada = Armada(IdArmada, nama, kapasitas)
        self.armada.append(armada)

    def getJumlahArmada(self):
        return len(self.armada)

    def isArmadaExist(self, idArmada):
        for IdArmada in self.IdArmada:
            if IdArmada.getIdArmada() == idArmada:
                return True
        return False
