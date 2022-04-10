# mundurin path dulu, biar controller bisa liat display
import sys
sys.path.append('../')
from  display.DisplaySignInSignUp.DisplaySignInSignUp import DisplaySignInSignUp 

class SignInSignUpController:
    def __init__(self):
        print("init invoked")
        self.display = DisplaySignInSignUp()
    def initiate(self):
        print("inititate invoked")
        action = self.display.show()
        return action

