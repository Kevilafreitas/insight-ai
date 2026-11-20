import json
from datetime import datetime, timezone, timedelta

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Fuso horário do Brasil (America/Sao_Paulo / UTC-3) com fallback seguro para Windows
try:
    from zoneinfo import ZoneInfo
    FUSO_BR = ZoneInfo("America/Sao_Paulo")
except Exception:
    FUSO_BR = timezone(timedelta(hours=-3))


def _agora_utc():
    return datetime.now(timezone.utc)


def _safe_json_loads(val):
    """Desserializa JSON de forma segura, evitando erros caso o campo esteja corrompido."""
    if not val:
        return []
    if isinstance(val, (list, dict)):
        return val
    try:
        return json.loads(val)
    except Exception:
        return []


class BatchAnalysis(db.Model):
    """Tabela para armazenar os relatórios gerados a partir de lotes de avaliações."""
    __tablename__ = 'batch_analyses'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(100), nullable=False, default="Parceiro Padrão")
    created_at = db.Column(db.DateTime, default=_agora_utc)
    total_reviews = db.Column(db.Integer, nullable=False)
    overall_sentiment = db.Column(db.String(50), nullable=False)

    # Dados estruturados guardados como JSON em texto
    top_complaints_json = db.Column(db.Text, nullable=False)
    operational_plan_json = db.Column(db.Text, nullable=False)
    customer_replies_json = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Converte o registro para dicionário (para enviar ao front-end)."""
        criado = self.created_at
        if criado is not None:
            # SQLite devolve datetime "ingênuo" (sem fuso): foi gravado em UTC
            if criado.tzinfo is None:
                criado = criado.replace(tzinfo=timezone.utc)
            try:
                criado_txt = criado.astimezone(FUSO_BR).strftime("%d/%m/%Y %H:%M")
            except Exception:
                criado_txt = criado.strftime("%d/%m/%Y %H:%M")
        else:
            criado_txt = "-"

        return {
            "id": self.id,
            "restaurant_name": self.restaurant_name,
            "created_at": criado_txt,
            "total_reviews": self.total_reviews,
            "overall_sentiment": self.overall_sentiment,
            "top_complaints": _safe_json_loads(self.top_complaints_json),
            "operational_plan": _safe_json_loads(self.operational_plan_json),
            "customer_replies": _safe_json_loads(self.customer_replies_json),
        }
