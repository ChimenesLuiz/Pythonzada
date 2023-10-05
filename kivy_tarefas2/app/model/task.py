import pyrebase

class Task:
    def __init__(self) -> None:
        self.config = ""
        self.firebase = ""


    def __connect(self) -> None:
        try:
            self.config = {
                    "apiKey": "AIzaSyABEIIYalUGSYScShyLf_lslWi1WZ84TPU",
                    "authDomain": "tasks-4e579.firebaseapp.com",
                    "databaseURL": "https://tasks-4e579-default-rtdb.firebaseio.com",
                    "projectId": "tasks-4e579",
                    "storageBucket": "tasks-4e579.appspot.com",
                    "messagingSenderId": "892908395026",
                    "appId": "1:892908395026:web:87c8bd25bd78fc9b8816cb"
                        }
            self.firebase = pyrebase.initialize_app(self.config)
        except:
            raise('Erro na hora de conectar!')
        

    def insertTask(self, data_p = dict) -> None:
        self.__connect()
        
        db = self.firebase.database()
        db.child("Taks").push(data = data_p)
        