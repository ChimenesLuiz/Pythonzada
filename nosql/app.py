import pyrebase
from getpass import getpass

class Banco:
    def __init__(self) -> None:
        self.config = ""
        self.firebase = ""

    def __connect(self) -> None:
        self.config = {
            "apiKey": "AIzaSyDbd4mIRfWndyj_DUPQ7g_A8Tze9I2R9dI",
            "authDomain": "taks-a3d13.firebaseapp.com",
            "databaseURL": "https://taks-a3d13-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId": "taks-a3d13",
            "storageBucket": "taks-a3d13.appspot.com",
            "messagingSenderId": "180738870160",
            "appId": "1:180738870160:web:2f06e5721a1c6519d64115",
            "measurementId": "G-VHD138KTGB"
            
                    }
        self.firebase = pyrebase.initialize_app(self.config)
        
    def createUser(self) -> bool:
        self.__connect()
        
        autentication = self.firebase.auth()
        
        email = "luizguichimenes2002@gmail.com"
        password = getpass("Password: ")
        if (autentication.create_user_with_email_and_password(email = email, password = password)):
            print("Usuario cadastrado com sucesso!")
            return True
        else:
            return False


    def cadastrarCollection(self) -> None:
        self.__connect()
        
        db = self.firebase.database()

        db.child("Data").push()
        
db = Banco()
db.cadastrarCollection()