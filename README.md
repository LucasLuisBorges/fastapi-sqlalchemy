# Cursos API - FastAPI + SQLAlchemy

API REST para gerenciamento de cursos usando FastAPI e SQLAlchemy com PostgreSQL assíncrono.

## 📋 Pré-requisitos

- Python 3.14+
- PostgreSQL
- pip

## 🚀 Instalação

### 1. Clone o repositório e navegue até a pasta

```bash
cd secao04
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres
```

Ajuste o usuário, senha, host, porta e nome do banco conforme sua configuração.

## 🗄️ Banco de Dados

### Inicie o PostgreSQL

**macOS (Homebrew):**
```bash
brew services start postgresql@14
```

**Linux:**
```bash
sudo systemctl start postgresql
```

**Docker:**
```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

### Crie as tabelas

```bash
python criar_tabelas.py
```

## ▶️ Executar a aplicação

```bash
python main.py
```

Ou com uvicorn diretamente:

```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🛣️ Endpoints

### Cursos

- `POST /api/v1/cursos/` - Criar novo curso
- `GET /api/v1/cursos/` - Listar todos os cursos
- `GET /api/v1/cursos/{id}` - Buscar curso por ID
- `PUT /api/v1/cursos/{id}` - Atualizar curso
- `DELETE /api/v1/cursos/{id}` - Deletar curso

### Exemplo de payload (POST/PUT):

```json
{
  "titulo": "Python Avançado",
  "aulas": 120,
  "horas": 40
}
```

## 📁 Estrutura do Projeto

```
secao04/
├── api/
│   └── v1/
│       ├── api.py
│       └── endpoints/
│           └── curso.py
├── core/
│   ├── configs.py      # Configurações da aplicação
│   ├── database.py     # Configuração do banco de dados
│   └── deps.py         # Dependências (sessions)
├── models/
│   └── curso_model.py  # Modelo SQLAlchemy
├── schemas/
│   └── curso_schema.py # Schemas Pydantic
├── criar_tabelas.py    # Script para criar tabelas
├── main.py             # Aplicação FastAPI
├── requirements.txt    # Dependências
└── .env                # Variáveis de ambiente
```

## 🔧 Tecnologias

- **FastAPI** - Framework web assíncrono
- **SQLAlchemy 2.0** - ORM com suporte assíncrono
- **AsyncPG** - Driver PostgreSQL assíncrono
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

## ⚠️ Troubleshooting

### Erro: "Connect call failed"
PostgreSQL não está rodando. Inicie o serviço conforme as instruções acima.

### Erro: "greenlet not found"
```bash
pip install greenlet
```

### Erro: "pydantic_settings not found"
```bash
pip install pydantic-settings
```

## 📝 Licença

Este projeto é parte de um curso educacional.
