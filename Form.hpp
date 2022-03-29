#include<iostream>
#include<string>
using namespace std;
class Form{

};
class FormSignUp : public Form{
    private:
        string username;
        string password;
        string Error;
    public:
        string show(){
            cout << "FormSignUp" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            if(Error != ""){
                void showError();
            }
            cout << "misalnya ini aksi submit" << endl;
            return onSubmit();

        }
        string onSubmit(){
            cout << "onSubmit" << endl;
            return "submit";
        }
        string getUsername(){
            return username;
        }
        string getPassword(){
            return password;
        }
        string getError(){
            return Error;
        }
        void setError(string error){
            Error = error;
        }
        void showError(){
            cout << Error << endl;
        }


};
class FormSignIn : public Form{
    private:
        string username;
        string password;
        string Error;
    public:
        string show(){
            cout << "FormSignIn" << endl;
            // didalem method show, dia bisa manggil method this lainnya, yang masing-masing bisa return ke controller
            cout << "misalnya ini aksi submit" << endl;
            return onSubmit();

        }
        string onSubmit(){
            cout << "onSubmit" << endl;
            return "submit";
        }
        string getUsername(){
            return username;
        }
        string getPassword(){
            return password;
        }
        string getError(){
            return Error;
        }
        void setError(string error){
            Error = error;
        }
};
class FormUbahArmada : public Form{

};
class FormTambahArmada : public Form{

};
class FormUbahRute : public Form{

};
class FormTambahRute : public Form{

};
