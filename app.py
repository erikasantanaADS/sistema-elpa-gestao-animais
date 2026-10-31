

from flask import Flask

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    return """
    <h1>Sistema ELPA - Gestão de Animais Resgatados</h1>
    <p>Bem-vindo ao sistema de cadastro e acompanhamento de animais.</p>
    <p>Projeto acadêmico em desenvolvimento.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
