import sqlite3

def conectar():
    return sqlite3.connect('locadora.db')

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            contato TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            qtd_disponivel INTEGER NOT NULL DEFAULT 0,
            valor_dia REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            equipamento_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL DEFAULT 1,
            data_inicio TEXT NOT NULL,
            data_fim TEXT,
            valor_total REAL,
            devolvido INTEGER DEFAULT 0,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (equipamento_id) REFERENCES equipamentos(id)
        )
    ''')

    conn.commit()
    conn.close()
