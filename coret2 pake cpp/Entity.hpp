#include<string>
using namespace std;
class Pengguna{
    private:
        string username; // PK
        string password;
        string role;// lebih cocok daripada 'status'
    public:
        Pengguna(string username, string password, string role){
            this->username = username;
            this->password = password;
            this->role = role;
        }
        string getUsername(){
            return this->username;
        }
        string getPassword(){
            return this->password;
        }
        string getRole(){
            return this->role;
        }

};
class Tiket{
    private:
        string idTiket; // PK
        string username;
        string idRute;
        string status; // menunggu pembayaran, sudah di bayar, cancel
        string tanggalPemesanan;
    public:
        Tiket(string idTiket, string idRute, string status, string tanggalPemesanan){
            this->idTiket = idTiket;
            this->idRute = idRute;
            this->status = status;
            this->tanggalPemesanan = tanggalPemesanan;
        }
        string getIdTiket(){
            return this->idTiket;
        }
        string getIdRute(){
            return this->idRute;
        }
        string getStatus(){
            return this->status;
        }
        string getTanggalPemesanan(){
            return this->tanggalPemesanan;
        }
        //tambahi setter

};
class Penumpang{
    private:
        string noKTP; // PK
        string nama;
        string noTelp;
        string idTiket; // FK
    public:
        Penumpang(string noKTP, string nama, string noTelp, string idTiket){
            this->noKTP = noKTP;
            this->nama = nama;
            this->noTelp = noTelp;
            this->idTiket = idTiket;
        }
        string getNoKTP(){
            return this->noKTP;
        }
        string getNama(){
            return this->nama;
        }
        string getNoTelp(){
            return this->noTelp;
        }
        string getIdTIket(){
            return this->idTiket;
        }
};
class Armada{
    private:
        string idArmada; // PK
        string nama;
        string kapasitas;
    public:
        Armada(string idArmada, string nama, string kapasitas){
            this->idArmada = idArmada;
            this->nama = nama;
            this->kapasitas = kapasitas;
        }
        string getIdArmada(){
            return this->idArmada;
        }
        string getNama(){
            return this->nama;
        }
        string getKapasitas(){
            return this->kapasitas;
        }
};
class Rute{
    private:
        string idRute; // PK
        string idArmada; // FK
        string idAsal; // FK
        string idTujuan; // FK
        string tanggalKeberangkatan;
        string jamBerangkat;
        string jamTiba;
        string harga;
    public:
        Rute(string idRute, string idArmada, string idAsal, string idTujuan, string tanggalKeberangkatan, string jamBerangkat, string jamTiba, string harga){
            this->idRute = idRute;
            this->idArmada = idArmada;
            this->idAsal = idAsal;
            this->idTujuan = idTujuan;
            this->tanggalKeberangkatan = tanggalKeberangkatan;
            this->jamBerangkat = jamBerangkat;
            this->jamTiba = jamTiba;
            this->harga = harga;
        }
        string getIdRute(){
            return this->idRute;
        }
        string getIdArmada(){
            return this->idArmada;
        }
        string getIdAsal(){
            return this->idAsal;
        }
        string getIdTujuan(){
            return this->idTujuan;
        }
        string getTanggalKeberangkatan(){
            return this->tanggalKeberangkatan;
        }
        string getJamBerangkat(){
            return this->jamBerangkat;
        }
        string getJamTiba(){
            return this->jamTiba;
        }
        string getHarga(){
            return this->harga;
        }
};
