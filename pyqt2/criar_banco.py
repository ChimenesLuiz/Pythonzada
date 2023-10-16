import sqlite3

# Conecte-se ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect('locadora.db')

# Crie um cursor para executar comandos SQL
cursor = conn.cursor()

# Crie uma tabela
cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT,
        telefone TEXT,
        cpf TEXT,
        cep TEXT,
        bairro TEXT,
        rua TEXT,
        numero TEXT
    )
''')



# Salve as alterações e feche a conexão
conn.commit()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY,
        ano TEXT,
        km TEXT,
        cambio TEXT,
        carroceria TEXT,
        combustivel TEXT,
        placa TEXT,
        cor TEXT,
        chassi TEXT
    )
''')

conn.commit()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS relacoes (
        id INTEGER PRIMARY KEY,
        id_usuario INT,
        id_veiculo INT,
        data_inicio DATETIME DEFAULT CURRENT_TIMESTAMP,
        data_limite DATETIME,
        preco DECIMAL,
        tipo TEXT
    )
''')
conn.commit()
conn.close()
