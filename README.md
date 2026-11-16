# InsightAI — Plataforma de IA Generativa para Análise de Feedbacks

O **InsightAI** é uma aplicação web desenvolvida em Python/Flask integrada ao modelo Gemini. A solução foi projetada para processar lotes de dados textuais não estruturados (como avaliações de clientes, chamados de suporte ou feedbacks de entrega) e transformá-los em dados estruturados contendo resumo, análise de sentimento, planos de ação recomendados e visualização em dashboards interativos.

🔗 **Aplicação Online:** [https://insight-ai-euwm.onrender.com](https://insight-ai-euwm.onrender.com)

---

## Problema & Caso de Uso

Em operações digitais de alto volume — como e-commerces, plataformas de delivery, SaaS e centrais de atendimento — milhares de avaliações e tickets de suporte são gerados diariamente. A leitura e triagem manual desses relatos atrasam a identificação de gargalos operacionais e a tomada de decisão das equipes de produto e suporte.

O **InsightAI** automatiza esse fluxo em três etapas:
- **Entrada:** Envio individual ou em lote de feedbacks e avaliações de clientes.
- **Processamento:** Extração de contexto, classificação de sentimento e geração de planos de ação utilizando IA Generativa com saída estruturada em JSON.
- **Saída:** Exibição de indicadores em dashboards, histórico de consultas e API REST para integração com outros sistemas.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Backend & API:** Flask, Gunicorn
- **Inteligência Artificial:** Google Gemini API
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Gerenciamento de Variáveis:** python-dotenv
- **Infraestrutura & Deploy:** Git, GitHub e Render

---

##  Arquitetura da Solução

```text
[ Interface Web / Cliente ] --( POST /api/analyze )--> [ Backend Flask (InsightAI) ]
                                                                |
                                                       [ Gemini Flash API ]
                                                                |
[ Dashboards & JSON ] <-----( Dados Estruturados )--------------+
