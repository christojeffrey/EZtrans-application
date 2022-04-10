#include "Entity.hpp"
class PenggunaManager{
    private:
        Pengguna* pengguna;
        int jumlahPengguna;
        int maxPengguna = 100;
    public:
        PenggunaManager();
        ~PenggunaManager();
        void addPengguna(Pengguna*){
            if(jumlahPengguna < maxPengguna){
                pengguna[jumlahPengguna] = *pengguna;
                jumlahPengguna++;
            }
        }
        
        bool isPenggunaExist(string username){
            for(int i = 0; i < jumlahPengguna; i++){
                if(pengguna[i].getUsername() == username){
                    return true;
                }
            }
            return false;
        }
        string getPassword(string username){
            for(int i = 0; i < jumlahPengguna; i++){
                if(pengguna[i].getUsername() == username){
                    return pengguna[i].getPassword();
                }
            }
            return "";
        }
        string getRole(string username){
            for(int i = 0; i < jumlahPengguna; i++){
                if(pengguna[i].getUsername() == username){
                    return pengguna[i].getRole();
                }
            }
            return "";
        }
};

class RuteManager{
    private:
        Rute* rute;
        int jumlahRute;
        int maxRute = 100;
    public:
        RuteManager();
        ~RuteManager();
        void addRute(Rute*){
            if(jumlahRute < maxRute){
                rute[jumlahRute] = *rute;
                jumlahRute++;
            }
        }
        
        bool isRuteExist(string idRute){
            for(int i = 0; i < jumlahRute; i++){
                if(rute[i].getIdRute() == idRute){
                    return true;
                }
            }
            return false;
        }

        //getter berdasarkan id rute, sesuai kebutuhan
       
};

class ArmadaManager{
    private:
        Armada* armada;
        int jumlahArmada;
        int maxArmada = 100;
    public:
        ArmadaManager();
        ~ArmadaManager();
        void addArmada(Armada*){
            if(jumlahArmada < maxArmada){
                armada[jumlahArmada] = *armada;
                jumlahArmada++;
            }
        }
        int getJumlahArmada(){
            return this->jumlahArmada;
        }
        bool isArmadaExist(string IdArmada){
            for(int i = 0; i < jumlahArmada; i++){
                if(armada[i].getIdArmada() == IdArmada){
                    return true;
                }
            }
            return false;
        }

        //getter berdasarkan kode armada, sesuai kebutuhan
       
};

class TiketManager{
    private:
        Tiket* tiket;
        int jumlahTiket;
        int maxTiket = 100;
    public:
        TiketManager();
        ~TiketManager();
        void addTiket(Tiket*){
            if(jumlahTiket < maxTiket){
                tiket[jumlahTiket] = *tiket;
                jumlahTiket++;
            }
        }
        
        bool isTiketExist(string idTiket){
            for(int i = 0; i < jumlahTiket; i++){
                if(tiket[i].getIdTiket() == idTiket){
                    return true;
                }
            }
            return false;
        }

        //getter berdasarkan id tiket, sesuai kebutuhan
       
};

class PenumpangManager{
    private:
        Penumpang* penumpang;
        int jumlahPenumpang;
        int maxPenumpang = 100;
    public:
        PenumpangManager();
        ~PenumpangManager();
        void addPenumpang(Penumpang*){
            if(jumlahPenumpang < maxPenumpang){
                penumpang[jumlahPenumpang] = *penumpang;
                jumlahPenumpang++;
            }
        }
        
        bool isPenumpangExist(string idPenumpang){
            for(int i = 0; i < jumlahPenumpang; i++){
                if(penumpang[i].getNoKTP() == idPenumpang){
                    return true;
                }
            }
            return false;
        }

        //getter berdasarkan id penumpang, sesuai kebutuhan
       
};