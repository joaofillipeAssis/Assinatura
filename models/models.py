from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date
from decimal import Decimal

class Assinatura(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal
