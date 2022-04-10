from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# directorynya harus digituin, soalnya yg manggil itu main :(
Form, Window = uic.loadUiType("form/FormSignUp/FormSignUp.ui")

class FormSignUp:
    def __init__(self):
        self.currentUsername = ""
        self.currentPassword = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
    def show(self, errorMessage):
        #bind
        self.form.signInButton.clicked.connect(self.signUpButtonClicked)
        self.form.errorMessageLabel.setText(errorMessage)
        # show
        self.window.show()
        self.app.exec()
        return self.currentUsername, self.currentPassword
    def signUpButtonClicked(self):
        self.currentUsername = self.form.usernameLineEdit.text()
        self.currentPassword = self.form.passwordLineEdit.text()
        self.window.close()
        print("Sign Up Button Clicked")
        