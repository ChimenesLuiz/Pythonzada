from entity.Banheiro import Banheiro
from entity.Outros import Outros

outros = Outros()

max_box = Outros.validarIntInput('Quantos box gostaria de adicionar')
if (max_box > 0):
    banheiro = Banheiro(max_box)
    banheiro.cadastrarBox()
else:
    banheiro = Banheiro(0)


while 1 == 1:
    banheiro.getBox()
    box = outros.validarIntInput(Outros.corLilas('ENTRE/SAIA'))
    if (box == 0):
        break
    banheiro.ocuparDesocupar(id =  box)



