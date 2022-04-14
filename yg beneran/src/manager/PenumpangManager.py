import sys
sys.path.append('../')
from entity.Penumpang import Penumpang

class PenumpangManager:
    def __init__(self):
        print("init tiket manager invoked")
        # array of tiket
        self.penumpang = []
    def addPenumpang(self, idPenumpang, namaPenumpang):
        penumpang = Penumpang(idPenumpang, namaPenumpang)
        self.penumpang.append(penumpang)
    def isPenumpangExist(self, idPenumpang):
        for penumpang in self.penumpang:
            if penumpang.getIdPenumpangt() == idPenumpang:
                return True
        return False
    
