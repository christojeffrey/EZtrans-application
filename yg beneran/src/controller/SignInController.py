import sys
sys.path.append('../')
from form.FormSignIn.FormSignIn import FormSignIn

class SignInController:
    def __init__(self):
        print("init sign in controller invoked")
        self.currentUsername = ""
        self.currentRole = ""
        self.errorMessage = ""
        self.display = FormSignIn()
    def initiate(self, penggunaManager):
        print("inititate sign in invoked")
        while(True):
            inputedUsername, inputedPassword = self.display.show(self.errorMessage)
            if(penggunaManager.isPenggunaExist(inputedUsername)):
                if(penggunaManager.isPasswordCorrect(inputedUsername, inputedPassword)):
                    self.currentUsername = inputedUsername
                    self.currentRole = penggunaManager.getRole(inputedUsername)
                    self.errorMessage = ""
                    break
                else:
                    self.errorMessage = "Password salah"
            else:
                self.errorMessage = "Username tidak ditemukan"

        return self.currentRole, self.currentUsername
