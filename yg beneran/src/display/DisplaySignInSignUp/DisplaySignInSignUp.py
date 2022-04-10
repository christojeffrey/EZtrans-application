from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# directorynya harus digituin, soalnya yg manggil itu main :(
Form, Window = uic.loadUiType("display/DisplaySignInSignUp/DisplaySignInSignUp.ui")



class DisplaySignInSignUp:
    def __init__(self):
        self.action = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
    def show(self):
        #bind
        self.form.signUpButton.clicked.connect(self.signUpButtonClicked)
        self.form.signInButton.clicked.connect(self.signInButtonClicked)
        # show
        self.window.show()
        self.app.exec()
        return self.action
    def signUpButtonClicked(self):
        print("Sign Up Button Clicked")
        self.action = "signup"
        self.window.close()
    def signInButtonClicked(self):
        print("Sign In Button Clicked")
        self.action = "signin"
        self.window.close()


