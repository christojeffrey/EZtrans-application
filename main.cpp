#include"Controller.hpp"
#include"Form.hpp"
#include"Manager.hpp"
#include"Display.hpp"

/*NOTE*/
//disini masih mengabaikan integrity constraint violation masih bisa terjadi (FK PK gk bener). buat menjaga integrity, hal ini diserahkan code
int main(){
    /*LOGIN SIGNUP*/
    //login controller and signup controller share the same pengguna manager
    //jadi manager harus dibikin global semua

    //make manager
    PenggunaManager penggunaManager = PenggunaManager();
    RuteManager ruteManager = RuteManager();
    ArmadaManager armadaManager = ArmadaManager();
    TiketManager tiketManager = TiketManager();
    PenumpangManager penumpangManager = PenumpangManager();

    //make controller
    SignUpController signUpController = SignUpController();

    SignInController signInController = SignInController();

    UbahRuteController ubahRuteController = UbahRuteController();
    TambahArmadaController tambahArmadaController = TambahArmadaController();
    UbahArmadaController ubahArmadaController = UbahArmadaController();
    TambahRuteController tambahRuteController = TambahRuteController();

    DisplayDaftarRuteController displayDaftarRuteController = DisplayDaftarRuteController();

    DisplayPesananController displayPesananController = DisplayPesananController();

    string action;
    //menampilkan homescreen dengan pilihan login atau signup
    // action = loginSignupController.initiateDisplay();
    //sementara gausah dulu, anggep ae wes tau mo login ato mo signup.
    string username; // to hold username
    if (action == "login"){
        username = signInController.initiateForm(penggunaManager);
    }
    else if (action == "signup"){
        username = signUpController.initiateForm(penggunaManager);
    }
    else{
        cout << "action tidak valid" << endl;
    }
    string role = penggunaManager.getRole(username);

    /*MASUK KE HOME DISPLAY*/
    //setelah login signup, masuk ke home
    HomeController homeController = HomeController();


    /*MASUK KE BAGIAN UTAMA*/
    //kalau admin, pilihannya form tambah armada, ubah armada, tambah rute, ubah rute, displaypesanan
    while(true){ // untuk membuat sederhananya, anggep aja gada exit dulu

        //masuk ke homescreen user ataupun admin
        action  = homeController.initiateForm(role, username);
        if(role == "admin"){
            if(action == "tambaharmada"){
                //tambah armada
                tambahArmadaController.initiateForm(armadaManager);
            }
            else if(action == "ubaharmada"){
                //ubah armada
                ubahArmadaController.initiateForm(armadaManager);
            }
            else if(action == "tambahrute"){
                //tambah rute
                tambahRuteController.initiateForm(ruteManager);
            }
            else if(action == "ubahrute"){
                //ubah rute
                ubahRuteController.initiateForm(ruteManager);
            }

            else if(action == "displaypesanan"){
                //display pesanan
                //butuh argumen pengguna, biar tau displaypesanan yg ditampilin itu punya user atau admin
                displayPesananController.initiateForm(role);
            }
            else{
                cout << "action tidak valid" << endl;
            }
        }
        else{ // pengguna == "user"
            if(action == "displaypesanan"){
                //display pesanan
                displayPesananController.initiateForm(role,username, tiketManager, penumpangManager);
            }
            else if(action == "displaydaftarrute"){
                string pilihanrute;
                //display daftar rute
                pilihanrute = displayDaftarRuteController.initiateForm(ruteManager);
                //habis itu, masuk ke form masukan penumpang
                pemesananTiketController.initiateForm(role, pilihanrute, ruteManager, tiketManager, penumpangManager);
            }
            else{
                cout << "action tidak valid" << endl;
            }
        }
    }
}