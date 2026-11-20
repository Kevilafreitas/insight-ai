# InsightAI — Copiloto de Gestão | Insights para Parceiros

O **InsightAI** é uma aplicação web desenvolvida em Python/Flask integrada ao modelo Gemini 3.8 Flash. A solução foi projetada para processar lotes de dados textuais não estruturados (como avaliações de clientes de restaurantes parceiros, feedbacks de entrega e chamados de suporte) e transformá-los em dados estruturados contendo resumo, análise de sentimento, principais gargalos operacionais agrupados, plano de ação recomendado e respostas profissionais prontas para clientes, exibidos em dashboards interativos e persistidos em SQLite.

🔗 **Aplicação Online:** [https://insight-ai-euwm.onrender.com](https://insight-ai-euwm.onrender.com)

---

## Problema & Caso de Uso

Em operações digitais de alto volume — como e-commerces, plataformas de delivery, SaaS e centrais de atendimento — centenas de avaliações e tickets de suporte são gerados diariamente. A leitura e triagem manual desses relatos atrasam a identificação de gargalos operacionais e a tomada de decisão das equipes de operações e atendimento.

O **InsightAI** automatiza esse fluxo em três etapas:
- **Entrada:** Envio individual ou em lote de avaliações e feedbacks de clientes (uma por linha).
- **Processamento:** Extração de contexto, classificação de sentimento e geração de planos de ação práticos utilizando o Google Gemini 3.8 Flash com saída rigorosamente estruturada em JSON via Pydantic schema.
- **Saída:** Exibição imediata em dashboard operacional, histórico persistido em banco SQLite e API REST para integração.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Backend & API:** Flask, SQLAlchemy (SQLite), Gunicorn
- **Inteligência Artificial:** Google GenAI SDK (`google-genai`), Gemini 3.8 Flash
- **Validação de Dados:** Pydantic
- **Frontend:** HTML5, CSS3, JavaScript (Dashboard responsivo)
- **Gerenciamento de Variáveis:** python-dotenv
- **Compatibilidade:** `tzdata` para suporte a fuso horário no Windows (`America/Sao_Paulo`)
- **Infraestrutura & Deploy:** Git, GitHub e Render

---

## Arquitetura da Solução

```text
[ Interface Web / Cliente ] --( POST /api/analyze-batch )--> [ Backend Flask (InsightAI) ]
                                                                       |
                                                           [ Gemini 3.8 Flash API ]
                                                                       |
[ Dashboards & Histórico ] <-----( JSON Estruturado )------------------+
```

---

## Estrutura do Projeto

```
app.py            # API Flask e integração com Google GenAI SDK
models.py         # Modelo BatchAnalysis (SQLAlchemy) e tratamento de timezone
templates/
  index.html      # Front-end (dashboard operacional responsivo)
requirements.txt  # Dependências do projeto (Flask, SQLAlchemy, GenAI, tzdata, gunicorn)
.env.example      # Modelo para variáveis de ambiente
.env              # Arquivo de configuração local (não versionado)
.gitignore        # Ignora venv/, .env, instance/ e caches
```

---

## Endpoints

- `GET /` — Interface web interativa
- `GET /api/history` — Últimas 10 análises salvas no SQLite
- `POST /api/analyze-batch` — Body JSON: `{"restaurant_name": "...", "reviews_text": "uma avaliação por linha"}`

---

## Como executar localmente

### 1. Clonar e preparar o ambiente virtual
```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar as dependências
```bash
pip install -r requirements.txt
```
> **Nota para Windows**: O pacote `tzdata` está incluído no `requirements.txt` para suporte nativo ao fuso horário `America/Sao_Paulo`.

### 3. Configurar as variáveis de ambiente
Copie o arquivo `.env.example` para `.env`:
```bash
copy .env.example .env    # Windows
# ou cp .env.example .env # Linux / macOS
```
Abra o `.env` e configure sua chave da API do Google Gemini obtida no [Google AI Studio](https://aistudio.google.com/):
```ini
GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-3.8-flash
FLASK_DEBUG=1
```

### 4. Executar a aplicação
```bash
python app.py
```
Acesse `http://127.0.0.1:5000`. O banco SQLite é inicializado automaticamente em `instance/partner_copilot.db`.

---

## Deploy em Produção (Linux / Render)

No Render ou servidores Linux, o comando de inicialização é:
```bash
gunicorn app:app
```

---

Autora: Kévila Freitas
