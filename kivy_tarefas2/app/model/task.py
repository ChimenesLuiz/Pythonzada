import pyrebase
import json as js
from getpass import getpass

class Task:
    def __init__(self) -> None:
        self.config = ""
        self.firebase = ""


    def __connect(self) -> None:
        try:
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
        except:
            raise('Erro na hora de conectar!')
        

    #private function
    def createUser(self, email_p = str, password_p = str) -> bool:
        self.__connect()

        autentication = self.firebase.auth()
        
        if (autentication.create_user_with_email_and_password(email = email_p, password = password_p)):
            return True
        else:
            return False

    
    def createTask(self, data_p = dict) -> None:
        self.__connect()
        
        db = self.firebase.database()
        db.child("Data").push(data = data_p)
        