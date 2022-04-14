class Tiket:
    def __init__(self, idTiket, idPenumpang, username, idRute, status, namaPenumpang, tanggalPemesanan):
        self.idTiket = idTiket
        self.idPenumpang = idPenumpang
        self.username = username
        self.idRute = idRute
        self.status = status
        self.namaPenumpang = namaPenumpang
        self.tanggalPemesanan = tanggalPemesanan
    def getIdTiket(self):
        return self.idTiket
    def getIdPenumpang(self):
        return self.getIdPenumpang
    def getUsername(self):
        return self.username
    def getIdRute(self):
        return self.idRute
    def getStatus(self):
        return self.status
    def getNamaPenumpang(self):
        return self.namaPenumpang
    def getTanggalPemesanan(self):
        return self.tanggalPemesanan
    def setIdTiket(self, idTaket):
        self.idTiket = idTaket
    def setIdPenumpang(self, idPenumpang):
        self.idPenumpang = idPenumpang
    def setUsername(self, username):
        self.username = username
    def setIdRute(self,idRute):
        self.idRute = idRute
    def setNamaPenumpang(self,namaPenumpang):
        self.namaPenumpang = namaPenumpang
    def setTanggalPemesanan(self, tanggalPemesanan):
        self.tanggalPemesanan = tanggalPemesanan
