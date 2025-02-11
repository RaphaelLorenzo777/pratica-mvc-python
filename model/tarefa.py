from database import Database

class Tarefa:
    def __init__(self, id, título, data_conclusão):
        self.id = id
        self.título = título
        self.data_conclusão = data_conclusão
        pass
    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()
      

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.título, self.data_conclusão)
        db.executar(sql, params)
        db.desconectar()
    
    def listarTarefas(self):
        """"Retorna uma lista de tarefas cadastradas no banco de dados."""
        db = Database()
        db.conectar()
     

        sql = 'SELECT id, titulo,data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()

        return tarefas if tarefas else[]
        
    def apagarTarefa(self):
        """Apaga uma tarefa cadastrada do banco de dados."""
        db = Database()
        db.conectar()
      

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (self.id,)
        db.executar(sql, params)
        db.desconectar()

tarefa = Tarefa(3, 'Teste de tarefa', None)
tarefa.apagarTarefa()

