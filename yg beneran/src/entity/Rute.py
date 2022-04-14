
class Rute:
    def __init__(self, idRute, idArmada, idAsal, idTujuan, tanggalKeberangkatan, jamBerangkat, durasi, harga, kapasitas):
        self.idRute = idRute
        self.idArmada = idArmada
        self.lokasiAwal = idAsal
        self.lokasiAkhir = idTujuan
        self.tanggalKeberangkatan = tanggalKeberangkatan
        self.jamBerangkat = jamBerangkat
        self.durasi = durasi
        self.harga = harga
        self.kapasitas = kapasitas

    def __str__(self):
        return "Rute:\nidRute: " + str(self.idRute) \
                    + "idArmada: " + str(self.idArmada) \
                    + "lokasiAwal: " + str(self.lokasiAwal) \
                    + "lokasiAkhir: " + str(self.lokasiAkhir) \
                    + "tanggalKeberangkatan: " + str(self.tanggalKeberangkatan) \
                    + "jamBerangkat: " + str(self.jamBerangkat) \
                    + "durasi: " + str(self.durasi) \
                    + "harga: " + str(self.harga) \
                    + "\n"

    def getIdRute(self):
        return self.idRute
    
    def getIdArmada(self):
        return self.idArmada
    
    def getLokasiAwal(self):
        return self.lokasiAwal
    
    def getLokasiAkhir(self):
        return self.lokasiAkhir
    
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

    def setIdRute(self, idRute):
        self.idRute = idRute

    def setIdArmada(self, idArmada):
        self.idArmada = idArmada
    
    def setlokasiAwal(self, idAsal):
        self.lokasiAwal = idAsal

    def setlokasiAkhir(self, idTujuan):
        self.lokasiAkhir = idTujuan

    def setTanggalKeberangkatan(self, tanggalKeberangkatan):
        self.tanggalKeberangkatan = tanggalKeberangkatan