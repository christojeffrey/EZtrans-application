from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# directorynya harus digituin, soalnya yg manggil itu main :(
Form, Window = uic.loadUiType("display/DisplayHome/DisplayAdminHome.ui")


class DisplayAdminHome:
    def __init__(self):
        self.action = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

    def show(self):
        # bind
        self.form.tambahRuteButton.clicked.connect(self.tambahRuteButton)
        # show
        self.window.show()
        self.app.exec()
        return self.action

    def tambahRuteButtonOnClick(self):
        print("Sign Up Button Clicked")
        self.action = "tambahrute"
        self.window.close()
