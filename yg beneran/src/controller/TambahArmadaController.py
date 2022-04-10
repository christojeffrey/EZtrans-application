from form.FormArmada.FormTambahArmada import FormArmada
import sys
sys.path.append('../')


class TambahArmadaController:
    def __init__(self):
        print("init tambah armada controller invoked")
        self.currentIdArmada = ""
        self.currentNama = ""
        self.currentKapasitas = ""
        self.errorMessage = ""
        self.display = FormArmada()

    def initiate(self, ArmadaManager):
        print("inititate tambah armada invoked")
        while(True):
            inputedIdArmada, inputedNama, inputedKapasitas = self.display.show(
                self.errorMessage)
            if(ArmadaManager.isPenggunaExist(inputedIdArmada)):
                self.errorMessage = "Armada sudah ada"
            else:
                ArmadaManager.addPengguna(
                    inputedIdArmada, inputedNama, inputedKapasitas)
                self.currentIdArmada = inputedIdArmada
                self.currentNama = inputedNama
                self.currentKapasitas = inputedKapasitas
                break
        return self.currentIdArmada, self.currentNama, self.currentKapasitas
