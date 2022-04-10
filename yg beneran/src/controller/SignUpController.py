import sys
sys.path.append('../')
from form.FormSignUp.FormSignUp import FormSignUp

class SignUpController:
    def __init__(self):
        print("init sign in controller invoked")
        self.currentUsername = ""
        self.currentRole = ""
        self.errorMessage = ""
        self.display = FormSignUp()
    def initiate(self, penggunaManager):
        print("inititate sign Up invoked")
        while(True):
            inputedUsername, inputedPassword = self.display.show(self.errorMessage)
            if(penggunaManager.isPenggunaExist(inputedUsername)):
                self.errorMessage = "Username sudah ada"
            else:
                penggunaManager.addPengguna(inputedUsername, inputedPassword, "user")
                self.currentUsername = inputedUsername
                self.currentRole = "user"
                self.errorMessage = ""
                break    
        return self.currentRole, self.currentUsername
