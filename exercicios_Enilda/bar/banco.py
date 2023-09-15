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
        status INTEGER,
        limite_tempo INTEGER
                            );
            """)

query = """
INSERT INTO boxes(status, limite_tempo) VALUES (?, ?)
        """
# for box in range(1, (self.total_box + 1)):
cursor.execute(query, (0, 0))

print('Tabela criada com sucesso.')
# desconectando...
conn.close()