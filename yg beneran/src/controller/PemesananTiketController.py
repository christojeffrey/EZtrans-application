import sys
sys.path.append('../')
from form.FormMasukanPenumpang.FormMasukanPenumpang import FormMasukanPenumpang

class PemesananTiketController:
    def __init__(self, idRute):
        print("init sign in controller invoked")
        self.penumpangList = [""]
        self.penumpangCount = 1 # dummy
        self.errorMessage = ""
        self.idRute = idRute
        self.display = FormMasukanPenumpang()
    def initiate(self, RuteManager):
        print("inititate pesan tiket invoked")
        while(True):
            if(RuteManager.isCapacityEnough(self.penumpangCount+1, self.idRute)):
                namaPenumpang = self.display.show(self.errorMessage)
                self.penumpangList.add(namaPenumpang)
            else:
                self.errorMessage = "Kapasitas penuh"
                namaPenumpang = self.display.show(self.errorMessage)
                break
           