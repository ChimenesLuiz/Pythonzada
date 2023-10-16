dicionario = {'chave_antiga': 'valor'}
# Chave que você deseja atualizar
chave_antiga = 'chave_antiga'
nova_chave = 'chave_nova'

# Criar um novo dicionário com a chave atualizada
novo_dicionario = {nova_chave: dicionario[chave_antiga]}

# Remover a chave antiga (opcional)
del dicionario[chave_antiga]

# Adicionar o novo dicionário ao orig