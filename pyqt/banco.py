import sqlite3

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect("larissa.db")

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        matricula INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT,
        telefone TEXT
    )
''')

# Commit para salvar as alterações e fechar a conexão
conn.commit()

# Fechar a conexão
conn.close()
