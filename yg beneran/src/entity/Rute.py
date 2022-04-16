
class Rute:
    def __init__(self, idRute, idArmada, idAsal, idTujuan, waktuKeberangkatan, durasi, harga, kapasitas):
        self.idRute = idRute
        self.idArmada = idArmada
        self.lokasiAwal = idAsal
        self.lokasiAkhir = idTujuan
        self.waktuKeberangkatan = waktuKeberangkatan
        self.durasi = durasi
        self.harga = harga
        self.kapasitas = kapasitas

    def __str__(self):
        return "Rute:\nidRute: " + str(self.idRute) \
                    + "idArmada: " + str(self.idArmada) \
                    + "lokasiAwal: " + str(self.lokasiAwal) \
                    + "lokasiAkhir: " + str(self.lokasiAkhir) \
                    + "waktuKeberangkatan: " + str(self.waktuKeberangkatan) \
                    + "durasi: " + str(self.durasi) \
                    + "harga: " + str(self.harga) \
                    + "kapasitas: " + str(self.kapasitas) \
                    + "\n"

    def getIdRute(self):
        return self.idRute
    
    def getIdArmada(self):
        return self.idArmada
    
    def getLokasiAwal(self):
        return self.lokasiAwal
    
    def getLokasiAkhir(self):
        return self.lokasiAkhir
    
    def getWaktuKeberangkatan(self):
        return self.waktuKeberangkatan
    
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

    def setWaktuKeberangkatan(self, waktuKeberangkatan):
        self.waktuKeberangkatan = waktuKeberangkatan