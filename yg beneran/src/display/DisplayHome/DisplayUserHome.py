from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# directorynya harus digituin, soalnya yg manggil itu main :(
Form, Window = uic.loadUiType("display/DisplayHome/DisplayUserHome.ui")


class DisplayAdminHome:
    def __init__(self):
        self.action = ""
        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

    def show(self):
        # bind
        self.form.lihatRuteButton.clicked.connect(self.lihatRuteButton)
        # show
        self.window.show()
        self.app.exec()
        return self.action

    def lihatRuteButtonOnClick(self):
        print("Lihat Rute Button Clicked")
        self.action = "lihatrute"
        self.window.close()
