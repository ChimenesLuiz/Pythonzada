from entity.Banheiro import Banheiro
from entity.Outros import Outros

outros = Outros()
banheiro = Banheiro(outros.validarInt('5'))

print('LUIZ`S BARS')

while 1 == 1:
    print(outros.corVerde('BOX 1\n---\nBOX 5'))
    box = outros.validarIntInput('Entre')
    banheiro.ocupar(box =  box)
    lista = banheiro.getBox()
    
    
    
    
    


