from flask import *

from Todo import *

todo = Todo()

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello world'


@app.route('/')
def list():
    return render_template('index.html', todoList=todo.getAllToto())


@app.route('/delete')
def delete():
    task = request.args.get('todo', '')
    todo.removeTodo(task)
    return render_template('index.html', todoList=todo.getAllToto())


@app.route('/insert', methods=['POST'])
def insert():
    task = request.form['todo']
    todo.addTodo(task)
    return render_template('index.html', todoList=todo.getAllToto())


if __name__ == '__main__':
    app.run(debug=True)
