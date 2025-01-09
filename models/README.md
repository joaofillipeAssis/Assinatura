## Instalar Models (ambiente para "base de dados")
```bash
pip install sqlmodel
```

Criação de classes que são convertidas em tabelas no banco de dados.


1. Primeiro, verifique se você está usando um ambiente virtual (venv). Se não estiver, crie um:

```bash
python -m venv venv
```

2. Ative o ambiente virtual:

No Windows:
```bash
venv\Scripts\activate
```

No Linux/Mac:
```bash
source venv/bin/activate
```

3. Instale o SQLModel com suas dependências:

```bash
pip install sqlmodel sqlalchemy typing-extensions
```

4. Verifique se a instalação foi bem-sucedida:

```bash
pip list | grep sqlmodel
```

Se após estes passos o erro persistir, pode ser um problema com seu IDE. Se estiver usando VS Code, tente:

1. Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no Mac)
2. Digite "Python: Select Interpreter"
3. Selecione o interpretador Python do seu ambiente virtual

## Executar o script database
```bash
python models/database.py
```

DATABASE é usado para configurar a estrutura do banco de dados.
Para manipular os registros execuar MODELS.

## Extensão Visualizar Banco de Dados
```bash
SQLite Viewer
```