import sqlite3

# Conectar-se ao banco de dados (isso criará o banco de dados se ele não existir)
conn = sqlite3.connect('todo.db')

# Criar um objeto cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task varcahr(50) NOT NULL, date varchar(50), completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)) DEFAULT 0)''')

# Commit (salvar) as alterações e fechar a conexão
conn.commit()
conn.close()
