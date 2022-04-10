class Pengguna:
    def __init__(self, idArmada, nama, kapasitas):
        self.idArmada = idArmada
        self.nama = nama
        self.kapasitas = kapasitas

    def getIdArmada(self):
        return self.idArmada

    def getNama(self):
        return self.nama

    def getKapasitas(self):
        return self.kapasitas
