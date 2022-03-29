//abstact base class, that's gonna have all the methods that are common to all the controllers
//controller is gonna be the class that have the ability to call form and display
#include "Form.hpp"
#include "Manager.hpp"
#include "Display.hpp"
class Controller {

};
class SignUpController : public Controller {
    private:
        FormSignUp form;
    public:
        string initiateForm(PenggunaManager penggunaManager){ // mengembalikan "user"
            while(true){
                string action = form.show();
                // controller can catch whatever it's that the form return
                //the action can pass an error to the form 
                if(action == "submit"){
                    //do something
                    bool res = this->validasiSignUp(penggunaManager);
                    //if everthing works the way it should
                    //then the controller will return to the main
                    if(res){
                        return "user"; //inget kalau signup cuman ada user
                    }
                    else{
                        //if everthing doesn't work the way it should
                        //then the controller will return to the form
                        continue;
                    }
                }

            }
        }
        bool validasiSignUp(PenggunaManager penggunaManager){
            //cek kalau user tidak ada dengan username tersebut belum terdaftar. kalau belum add new pengguna
            //kalau sudah, return false
            string username = form.getUsername();
            string password = form.getPassword();

            if(penggunaManager.isPenggunaExist(username)){
                form.setError("Username sudah terdaftar");
                return false;
            }
            else{
                penggunaManager.addPengguna(new Pengguna(username, password, "user"));
                return true;
            }  
        }
};
class SignInController : public Controller {
    private:
        FormSignIn form;
    public:
        string initiateForm(PenggunaManager penggunaManager){ // mengembalikan "user" atau "admin"
            while(true){
                string action = form.show();
                // controller can catch whatever it's that the form return
                //the action can pass an error to the form 
                if(action == "submit"){
                    //do something
                    //res berupa string, "user" atau "admin"
                    string res = this->validasiSignIn(penggunaManager);
                    //if everthing works the way it should
                    //then the controller will return to the main
                    if(res == "user"){
                        return "user";
                    }
                    else if(res == "admin"){
                        return "admin";
                    }
                    else{
                        //if everthing doesn't work the way it should
                        //then the controller will return to the form
                        continue;
                    }
                }

            }
        }
        string validasiSignIn(PenggunaManager penggunaManager){
            //cek kalau user tidak ada dengan username tersebut belum terdaftar. kalau belum, error
            string username = form.getUsername();
            string password = form.getPassword();
            if(penggunaManager.isPenggunaExist(username)){
                if(penggunaManager.getPassword(username) == password){
                    return "user";
                }
                else{
                    form.setError("Password salah");
                    return "";
                }
            }
            else{
                form.setError("Username tidak terdaftar");
                return "";
            }
        }
          
       
};

class HomeController : public Controller {
    private:
        DisplayAdminHome displayAdmin;
        DisplayUserHome displayUser;
    public:
        string initiateForm(string role,string pengguna){
            this->displayAdmin = DisplayAdminHome();
            this->displayUser = DisplayUserHome();
            
            return "";
        }
};

class TambahRuteController : public Controller {
    private:
        FormTambahRute form;
    public:
        string initiateForm(RuteManager ruteManager){
        }
};

class UbahRuteController : public Controller {
    private:
        FormUbahRute form;
    public:
        string initiateForm(RuteManager ruteManager){
        }
};

class TambahArmadaController : public Controller {
    private:
        FormTambahArmada form;
    public:
        string initiateForm(ArmadaManager armadaManager){
        }
};
class UbahArmadaController : public Controller {
    private:
        FormUbahArmada form;
    public:
        string initiateForm(ArmadaManager armadaManager){
        }
};

class DisplayDaftarRuteController : public Controller {
    private:
        DisplayDaftarRute display;
    public:
        string initiateForm(RuteManager ruteManager){
            //menampilkan pilihan rute, mengembalikan id pilihan rute yg dipilih
        }
};

class DisplayPesananController : public Controller {
    private:
        DisplayPesanan display;
    public:
        string initiateForm(string role, string username, TiketManager tiketManager,PenumpangManager penumpangManager){
        }
    
};

class PemesananTiketController : public Controller {
    private:
        FormMasukanPenumpang form;
    public:
        string initiateForm(string username, string pilihanrute, RuteManager ruteManager, TiketManager tiketManager,PenumpangManager penumpangManager){
        }
        
};