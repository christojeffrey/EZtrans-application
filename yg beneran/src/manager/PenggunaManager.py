import sys
sys.path.append('../')
from entity.Pengguna import Pengguna

class PenggunaManager:
    def __init__(self):
        print("init pengguna manager invoked")
        #array of pengguna
        self.pengguna = []
    def addPengguna(self, username, password, role):
        pengguna = Pengguna(username, password, role)
        self.pengguna.append(pengguna)
    def isPenggunaExist(self, username):
        for pengguna in self.pengguna:
            if pengguna.getUsername() == username:
                return True
        return False
    def getRole(self, username):
        for pengguna in self.pengguna:
            if pengguna.getUsername() == username:
                return pengguna.getRole()
        return None
    def isPasswordCorrect(self, username, password):
        for pengguna in self.pengguna:
            if pengguna.getUsername() == username and pengguna.getPassword() == password:
                return True
        return False
    
