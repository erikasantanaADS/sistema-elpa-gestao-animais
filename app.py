
from datetime import date
from flask import Flask, render_template, request, redirect, url_for
from banco import conectar, criar_tabelas

app = Flask(__name__)

criar_tabelas()


@app.route("/")
def pagina_inicial():
    return render_template("index.html")


@app.route("/cadastrar-animal", methods=["GET", "POST"])
def cadastrar_animal():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        especie = request.form.get("especie", "").strip()
        idade = request.form.get("idade", "").strip()
        data_resgate = request.form.get("data_resgate", "").strip()
        saude = request.form.get("saude", "").strip()
        status = request.form.get("status", "").strip()

        if especie not in ["Cachorro", "Gato", "Outro"]:
            return "Espécie inválida.", 400

        if status not in [
            "em tratamento",
            "disponível para adoção",
            "adotado"
        ]:
            return "Situação de adoção inválida.", 400

        try:
            data = date.fromisoformat(data_resgate)
            if data > date.today():
                return "A data do resgate não pode ser futura.", 400
        except ValueError:
            return "Data do resgate inválida.", 400

        conexao = conectar()
        try:
            conexao.execute("""
                INSERT INTO animais
                (nome, especie, idade, data_resgate, saude, status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, especie, idade, data_resgate, saude, status))
            conexao.commit()
        finally:
            conexao.close()

        return redirect(url_for("cadastro_sucesso"))

    return render_template("cadastrar_animal.html")


@app.route("/cadastro-sucesso")
def cadastro_sucesso():
    return """
    <h1>Animal cadastrado com sucesso!</h1>
    <p>As informações foram salvas no Sistema ELPA.</p>
    <a href="/cadastrar-animal">Cadastrar outro animal</a>
    <p><a href="/consultar-animais">Consultar animais</a></p>
    <p><a href="/">Voltar ao menu principal</a></p>
    """


@app.route("/consultar-animais")
def consultar_animais():
    conexao = conectar()
    try:
        animais = conexao.execute("""
            SELECT * FROM animais ORDER BY id DESC
        """).fetchall()
    finally:
        conexao.close()

    return render_template(
        "consultar_animais.html",
        animais=animais
    )


@app.route("/atendimento-veterinario", methods=["GET", "POST"])
def atendimento_veterinario():
    conexao = conectar()

    try:
        if request.method == "POST":
            animal_id = request.form.get("animal_id", "").strip()
            data_atendimento = request.form.get(
                "data_atendimento", ""
            ).strip()
            veterinario = request.form.get("veterinario", "").strip()
            descricao = request.form.get("descricao", "").strip()
            tratamento = request.form.get("tratamento", "").strip()

            if not animal_id.isdigit():
                return "Selecione um animal válido.", 400

            animal = conexao.execute(
                "SELECT id FROM animais WHERE id = ?",
                (int(animal_id),)
            ).fetchone()

            if animal is None:
                return "Animal não encontrado.", 404

            try:
                data = date.fromisoformat(data_atendimento)
                if data > date.today():
                    return "A data do atendimento não pode ser futura.", 400
            except ValueError:
                return "Data do atendimento inválida.", 400

            if not descricao:
                return "Informe a descrição do atendimento.", 400

            conexao.execute("""
                INSERT INTO atendimentos
                (animal_id, data_atendimento, veterinario,
                 descricao, tratamento)
                VALUES (?, ?, ?, ?, ?)
            """, (
                int(animal_id),
                data_atendimento,
                veterinario,
                descricao,
                tratamento
            ))
            conexao.commit()

            return redirect(url_for("atendimento_sucesso"))

        animais = conexao.execute("""
            SELECT id, nome, especie
            FROM animais ORDER BY nome
        """).fetchall()

    finally:
        conexao.close()

    return render_template(
        "atendimento_veterinario.html",
        animais=animais
    )


@app.route("/atendimento-sucesso")
def atendimento_sucesso():
    return """
    <h1>Atendimento veterinário registrado com sucesso!</h1>
    <p>As informações foram salvas no banco de dados.</p>
    <a href="/atendimento-veterinario">Novo atendimento</a>
    <p><a href="/historico-veterinario">Consultar histórico</a></p>
    <p><a href="/">Voltar ao menu principal</a></p>
    """


@app.route("/historico-veterinario")
def historico_veterinario():
    conexao = conectar()

    try:
        animais = conexao.execute("""
            SELECT id, nome, especie
            FROM animais ORDER BY nome
        """).fetchall()

        animal_id_texto = request.args.get("animal_id", "")
        animal_id = None
        atendimentos = []

        if animal_id_texto.isdigit():
            animal_id = int(animal_id_texto)

            animal_existe = conexao.execute(
                "SELECT id FROM animais WHERE id = ?",
                (animal_id,)
            ).fetchone()

            if animal_existe is None:
                return "Animal não encontrado.", 404

            atendimentos = conexao.execute("""
                SELECT data_atendimento, veterinario,
                       descricao, tratamento
                FROM atendimentos
                WHERE animal_id = ?
                ORDER BY data_atendimento DESC, id DESC
            """, (animal_id,)).fetchall()

    finally:
        conexao.close()

    return render_template(
        "historico_veterinario.html",
        animais=animais,
        animal_id=animal_id,
        atendimentos=atendimentos
    )


@app.route("/atualizar-adocao", methods=["GET", "POST"])
def atualizar_adocao():
    conexao = conectar()

    try:
        mensagem = None

        if request.method == "POST":
            animal_id = request.form.get("animal_id", "").strip()
            novo_status = request.form.get("status", "").strip()

            status_validos = [
                "em tratamento",
                "disponível para adoção",
                "adotado"
            ]

            if not animal_id.isdigit():
                return "Selecione um animal válido.", 400

            if novo_status not in status_validos:
                return "Situação de adoção inválida.", 400

            animal = conexao.execute(
                "SELECT id FROM animais WHERE id = ?",
                (int(animal_id),)
            ).fetchone()

            if animal is None:
                return "Animal não encontrado.", 404

            conexao.execute("""
                UPDATE animais
                SET status = ?
                WHERE id = ?
            """, (novo_status, int(animal_id)))

            conexao.commit()
            mensagem = "Situação de adoção atualizada com sucesso!"

        animais = conexao.execute("""
            SELECT id, nome, especie, status
            FROM animais
            ORDER BY nome
        """).fetchall()

    finally:
        conexao.close()

    return render_template(
        "atualizar_adocao.html",
        animais=animais,
        mensagem=mensagem
    )


@app.route("/sobre")
def sobre():
    return """
    <h1>Sobre o Sistema ELPA</h1>
    <p>Projeto acadêmico de Análise e Desenvolvimento de Sistemas.</p>
    <p>Objetivo: apoiar o cadastro, acompanhamento veterinário
    e gestão de adoção de animais resgatados.</p>
    <p>Esta é uma versão inicial em desenvolvimento.</p>
    <a href="/">Voltar à página inicial</a>
    """


if __name__ == "__main__":
    app.run(debug=False)
