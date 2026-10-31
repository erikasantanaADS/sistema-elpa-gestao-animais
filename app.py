

from flask import Flask

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    return """
    <h1>Sistema ELPA - Gestão de Animais Resgatados</h1>
    <p>Bem-vindo ao sistema de cadastro e acompanhamento de animais.</p>
    <p>Projeto acadêmico em desenvolvimento.</p>
    """

@app.route("/sobre")
def sobre():
    return """
    <h1>Sobre o Sistema ELPA</h1>
    <p>Projeto acadêmico de Análise e Desenvolvimento de Sistemas.</p>
    <p>Objetivo: desenvolver um sistema para apoiar o cadastro,
    o acompanhamento veterinário e a gestão da adoção
    de animais resgatados.</p>
    <p>Esta é uma versão inicial em desenvolvimento.</p>
    <a href="/">Voltar à página inicial</a>
    """
if __name__ == "__main__":
    app.run(debug=True)
