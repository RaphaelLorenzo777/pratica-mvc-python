from model.database import Database
 
class Tarefa:

    def __init__(self, id=None, titulo=None, data_conclusao=None):

        self.id = id

        self.titulo = titulo

        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):

        """Salva uma nova tarefa no banco de dados."""

        db = Database()

        db.conectar()
 
        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'

        params = (self.titulo, self.data_conclusao)

        db.executar(sql, params)

        db.desconectar()
 
    @staticmethod

    def listarTarefas():

        """Retorna uma lista de tarefas cadastradas."""

        db = Database()

        db.conectar()
 
        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'

        tarefas = db.consultar(sql)

        db.desconectar()

        return tarefas if tarefas else []
 
    def apagarTarefa(self):

        """Apaga uma tarefa cadastrada no banco de dados."""

        db = Database()

        db.conectar()
 
        sql = 'DELETE FROM tarefa WHERE id = %s'

        params = (self.id,)  # Corrigir como tupla

        db.executar(sql, params)

        db.desconectar()
 