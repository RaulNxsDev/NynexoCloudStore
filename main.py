from flask import Flask, render_template

app = Flask(__name__)

services = [
    {"nome": "Government Logs", "descricao": "Logins Governamentais de diversos países colhidos diariamente."},
    {"nome": "Stream Logs", "descricao": "Logins De Diversos Streamings De Boa Qualidade."},
    {"nome": "Game Logs", "descricao": "Logins De Diversos Jogos Em Sua Versão Mobile."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', services=services)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(debug=True)