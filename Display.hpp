#include<string>
#include<iostream>
using namespace std;
class DisplayLoginSignup{
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
            cout << "misalnya dia tambah tiket" << endl;
            return tambahTiketButtonOnClick();
        }
        string tambahTiketButtonOnClick(){
            return "tambahtiket";
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

class DisplayPesanan{
    public:
        string show(){
            cout << "displayPesanan" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            return "";
        }
};