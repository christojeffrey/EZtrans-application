
class Rute:
    def __init__(self, idRute, idArmada, idAsal, idTujuan, tanggalKeberangkatan, jamBerangkat, jamTiba, harga, kapasitas):
        self.idRute = idRute
        self.idArmada = idArmada
        self.idAsal = idAsal
        self.idTujuan = idTujuan
        self.tanggalKeberangkatan = tanggalKeberangkatan
        self.jamBerangkat = jamBerangkat
        self.jamTiba = jamTiba
        self.harga = harga
        self.kapasitas = kapasitas

    def __str__(self):
        return "Rute:\nidRute: " + str(self.idRute) \
                    + "idArmada: " + str(self.idArmada) \
                    + "idAsal: " + str(self.idAsal) \
                    + "idTujuan: " + str(self.idTujuan) \
                    + "tanggalKeberangkatan: " + str(self.tanggalKeberangkatan) \
                    + "jamBerangkat: " + str(self.jamBerangkat) \
                    + "jamTiba: " + str(self.jamTiba) \
                    + "harga: " + str(self.harga) \
                    + "\n"

    def getIdRute(self):
        return self.idRute
    
    def getIdArmada(self):
        return self.idArmada
    
    def getIdAsal(self):
        return self.idAsal
    
    def getIdTujuan(self):
        return self.idTujuan
    
    def getTanggalKeberangkatan(self):
        return self.tanggalKeberangkatan
    
    def getJamBerangkat(self):
        return self.jamBerangkat
    
    def getJamTiba(self):
        return self.jamTiba
    
    def getHarga(self):
        return self.harga

    def getKapasitas(self):
        return self.kapasitas

# if __name__ == "__main__":