import os
from sqlite3 import connect

class DatabaseManager:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__),"Dados Default.db")
        self.db = connect(self.db_path)
        self.cursor = self.db.cursor()

        ### Se não existir, cria a tabela para armazenamento das pastas:
        ### ID(INT) | NOME(TEXT)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pastas (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT NOT NULL)''')

        ### Commit do Banco de Dados
        self.db.commit()

    ### -------------------------------------------------------------------------
    ### Funções para gerenciamento de Pastas
    ### -------------------------------------------------------------------------
    def _criar_nova_pasta(self,nome):
        self.cursor.execute('INSERT INTO pastas (nome) VALUES (?)',(nome,))
        self.db.commit()
        return self.cursor.lastrowid
    
    def _apagar_pasta_existente(self,id):
        self.cursor.execute('DELETE FROM pastas WHERE id = ?',(id,))
        self.db.commit()

    def _renomear_pasta_existente(self,id,nome):
        self.cursor.execute('UPDATE pastas SET nome = ? WHERE id = ?',(nome,id))
        self.db.commit()

    def _buscar_pastas_existentes(self):
        self.cursor.execute('SELECT id, nome FROM pastas')
        return self.cursor.fetchall()
