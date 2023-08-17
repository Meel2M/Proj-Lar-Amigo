from flask import Flask, render_template, request, redirect, url_for, session
#flask - oque traz a biblioteca, as regras
#render_template -apresenta um arquivo html, redenizar
#request - toda vez q for requisição
#redirect - redirecionar a pessoa para outra pagina
#url_for - msm coisa de hf, caminho que deve seguir

#obrigatorio ter para inicialização do servidor do flask
app = Flask(__name__)


@app.route('/sucesso', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cpf = request.form['cpf']
        session['mensagem'] = "Cadastro realizado com sucesso!!"
    return render_template('contato.html', session)

if __name__ == "__main__":
    app.run(debug=True)
