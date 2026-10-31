
import sqlite3

NOME_BANCO = "elpa.db"


def conectar():
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabelas():
    conexao = conectar()

    try:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS animais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                especie TEXT NOT NULL,
                idade TEXT,
                data_resgate TEXT NOT NULL,
                saude TEXT,
                status TEXT NOT NULL
            )
        """)

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS atendimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_id INTEGER NOT NULL,
                data_atendimento TEXT NOT NULL,
                veterinario TEXT,
                descricao TEXT NOT NULL,
                tratamento TEXT,
                FOREIGN KEY (animal_id)
                    REFERENCES animais(id)
            )
        """)

        conexao.commit()
    finally:
        conexao.close()


if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados do Sistema ELPA atualizado com sucesso!")
