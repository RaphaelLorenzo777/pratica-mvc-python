from flask import Flask, redirect, render_template, request, url_for
from model.tarefa import Tarefa
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':

        titulo = request.form['titulo']

        data_conclusao = request.form['data_conclusao']

        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)

        tarefa.salvarTarefa()

        return redirect(url_for('index'))
 
    tarefas = Tarefa.listarTarefas()

    return render_template("index.html", tarefas=tarefas, title='Minhas Tarefas')
 
@app.route('/delete/<int:idtarefa>')

def delete(idtarefa):

    tarefa = Tarefa(id=idtarefa)  # Passando o parâmetro correto 'id' para o construtor

    tarefa.apagarTarefa()  # Chama o método para apagar a tarefa

    return redirect(url_for('index'))
 