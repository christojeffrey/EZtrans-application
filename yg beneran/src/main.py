# future improvement yg gk perlu kita cover
# 1. add back button, and appState. back button ngeganti nilai dari appState
# 2. setiap kali ganti display atau form, windownya ke close, trus ke open lagi. bagusnya ya gk ke close. 

#import controller
from controller.SignInSignUpController import SignInSignUpController
from controller.SignInController import SignInController
from controller.SignUpController import SignUpController

#import manager
from manager.PenggunaManager import PenggunaManager

# STAGE SETUP
# KAMUS
action = ""
currentUsername = ""
currentRole = ""
# create instance of manager
penggunaManager = PenggunaManager()
# add dummy data to manager
penggunaManager.addPengguna("admin", "admin123", "admin")
penggunaManager.addPengguna("user", "user123", "user")
# STAGE SIGN UP SIGN IN
signInSignUpController = SignInSignUpController()
action = signInSignUpController.initiate()

# STAGE SIGN UP
if(action == "signup"):
    print("signup")
    signUpController = SignUpController()
    currentRole, currentUsername = signUpController.initiate(penggunaManager)

# STAGE SIGN IN
elif(action == "signin"):
    print("signin")
    signInController = SignInController()
    currentRole, currentUsername = signInController.initiate(penggunaManager)

# STAGE HOME
print("currentRole: " + currentRole)
print("currentUsername: " + currentUsername)


