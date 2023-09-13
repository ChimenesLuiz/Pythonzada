from entity.Outros import Outros

class Banheiro:
    def __init__(self, total_box = int) -> None:
        self.total_box = total_box
        self.box = {}
        for c in range(1, (self.total_box) + 1):
            self.box[c] = 0
            
    def ocupar(self, box = int) -> None:
        for key in self.box.keys():
            if (box == key):
                self.box[key] = 1
                break
    
    def getBox(self):
        Outros.clearTerminal()
        for c in self.box.keys():
            print('-'*30)
            print(f"BOX {c}: {print('OCUPADO') if c == 1 else print('LIVRE')}")
        print('-'*30)
        