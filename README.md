# Sistema ELPA – Gestão de Animais Resgatados

Projeto acadêmico desenvolvido para a disciplina de Projeto de Software do curso de Análise e Desenvolvimento de Sistemas.

## Objetivo

Desenvolver um MVP de sistema web para auxiliar no cadastro, acompanhamento veterinário e controle da situação de adoção de animais resgatados.

O Instituto Eu Luto Pelos Animais (ELPA) foi utilizado como referência para o estudo, sem vínculo institucional confirmado.

## Tecnologias

- Python 3.12
- Flask
- Flask-Login
- SQLite (previsto para a persistência de dados)
- HTML, CSS e JavaScript (previstos para a interface)

## Como executar a versão inicial

1. Instale Python 3.12.
2. Crie e ative um ambiente virtual.
3. Instale as dependências com:
   pip install -r requirements.txt
4. Execute:
   python app.py
5. Acesse http://127.0.0.1:5000 no navegador.

## Estado atual

A aplicação Flask já apresenta uma página inicial simples. As funcionalidades de cadastro, consulta e acompanhamento dos animais ainda estão em desenvolvimento.

## Revisão técnica do MVP

### Arquitetura
O Sistema ELPA foi desenvolvido com Python e Flask, utilizando páginas HTML para a interface e SQLite para o armazenamento dos dados. A aplicação possui funcionalidades de cadastro e consulta de animais, registro de atendimentos veterinários, consulta do histórico e atualização da situação de adoção.

### Legibilidade e organização
O projeto utiliza arquivos separados para a aplicação Python, a configuração do banco de dados, as páginas HTML e os estilos CSS. Essa organização facilita a leitura, a manutenção e a evolução do sistema.

### Segurança
Durante a revisão, foi identificada a necessidade de aprimorar a segurança da aplicação, incluindo autenticação de usuários, controle de acesso, validação dos dados recebidos e desativação do modo de depuração em ambiente de produção.

### Melhorias futuras
Como evolução do MVP, estão previstas a implementação de login, a melhoria das validações, a criação de testes automatizados e o aperfeiçoamento das mensagens de erro.

### Conclusão da auto-revisão
A revisão permitiu identificar pontos positivos da estrutura atual e melhorias necessárias para futuras versões. O MVP atende às funcionalidades principais propostas para esta etapa acadêmica.
