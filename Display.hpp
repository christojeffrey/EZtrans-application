#include<string>
#include<iostream>
using namespace std;
class DisplaySignInSignUp{
    public:
        string show(){
            cout << "DisplayLoginSignup" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            cout << "misalnya login"<< endl;
            return loginButtonOnClick();
        }
        string loginButtonOnClick(){
            return "login";
        }
        string signupButtonOnClick(){
            return "signup";
        }
};

class DisplayAdminHome{
    public:
        string show(){
            cout << "displayAdminHome" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
           cout << "misalnya dia tambah rute" << endl;
            return tambahRuteButtonOnClick();
        }
      
        string tambahRuteButtonOnClick(){
            return "tambahrute";
        }
};
class DisplayUserHome{
    public:
        string show(){
            cout << "displayUserHome" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            //misalnya dia melihat rute
            cout << "misalnya dia melihat rute" << endl;
            return lihatRuteButtonOnClick();
        }
        string lihatRuteButtonOnClick(){
            return "lihatrute";
        }
};

class DisplayRiwayat{
    public:
        string show(){
            cout << "displayPesanan" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};
class DisplayDetailRiwayat{
    public:
        string show(){
            cout << "displayDetailPesanan" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};

class DisplayDaftarRute{
    public:
        string show(){
            cout << "displayDaftarRute" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};
class DisplayDetailRute{
    public:
        string show(){
            cout << "displayDetailRute" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};

class DisplayDetailPesanan{
    public:
        string show(){
            cout << "displayDetail" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};

class DisplayPembayaran{
    public:
        string show(){
            cout << "displayPembayaran" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};

