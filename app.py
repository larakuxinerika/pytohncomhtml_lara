from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = "Turma de Programação"
    curso = "Python = HTML"

    return render_template(
    'index.html',
    name = nome,
    curso = curso
)

@app.route('/sobre')
def sobre():
    return"""
    <h1>Sobre a Turma</h1>
    <p>Esse projeto foi criado usando python e HTML.</p>
    <a href="/">Voltar para o início</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)