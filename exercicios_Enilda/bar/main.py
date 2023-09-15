from entity.Banheiro import Banheiro
from entity.Outros import Outros

outros = Outros()

max_box = Outros.validarIntInput('Quantos box gostaria de adicionar')
banheiro = Banheiro(max_box)
banheiro.cadastrarBox()

print('LUIZ`S BARS')

# while 1 == 1:
#     banheiro.getBox()
#     box = outros.validarIntInput('Entre/Saia')
#     banheiro.ocupar(box =  box)



