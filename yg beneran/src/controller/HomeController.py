from display.DisplayHome.DisplayAdminHome import DisplayAdminHome
from display.DisplayHome.DisplayUserHome import DisplayUserHome
import sys
sys.path.append('../')


class HomeController:
    def __init__(self):
        print("init invoked")
        self.displayAdmin = DisplayAdminHome()
        self.displayUser = DisplayUserHome()

    def initiate(self, role):
        if(role == "user"):
            action = self.displayUser.show()
        elif(role == "admin"):
            action = self.displayAdmin.show()
        print("inititate invoked")
        return action
