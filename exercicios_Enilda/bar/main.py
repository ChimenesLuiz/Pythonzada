from entity.Banheiro import Banheiro
from entity.Outros import Outros

outros = Outros()

banheiro = Banheiro(Outros.validarInt(5))

print('LUIZ`S BARS')

while 1 == 1:
    banheiro.getBox()
    box = outros.validarIntInput('Entre/Saia')
    banheiro.ocupar(box =  box)



