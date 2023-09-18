# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('banheiros.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
        CREATE TABLE boxes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        status INTEGER
                            );
            """)

print('Tabela criada com sucesso.')
# desconectando...
conn.close()