# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('banco.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
        CREATE TABLE banheiros(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        total_box INTEGER,
        status,
        limite_tempo INTEGER,
        data_criacao DATE NOT NULL
                            );
            """)

print('Tabela criada com sucesso.')
# desconectando...
conn.close()