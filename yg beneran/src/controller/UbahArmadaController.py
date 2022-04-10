from form.FormArmada.FormUbahArmada import FormArmada
import sys
sys.path.append('../')


class UbahArmadaController:
    def __init__(self):
        print("init ubah armada controller invoked")
        self.currentIdArmada = ""
        self.currentNama = ""
        self.currentKapasitas = ""
        self.errorMessage = ""
        self.display = FormArmada()

    def initiate(self, ArmadaManager):
        print("inititate ubah armada invoked")
        while(True):
            inputedIdArmada, inputedNama, inputedKapasitas = self.display.show(
                self.errorMessage)
            if(ArmadaManager.isPenggunaExist(inputedIdArmada)):
                self.currentIdArmada = inputedIdArmada
                self.currentNama = inputedNama
                self.currentKapasitas = inputedKapasitas
            else:
                self.errorMessage = "Armada tidak ada"
                break
        return self.currentIdArmada, self.currentNama, self.currentKapasitas
