from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import date
from decimal import Decimal

class Assinatura(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal

class Pagamento(SQLModel, table=True):
    id: int = Field(primary_key=True)
    # assinatura.id = campo id da classe Assinatura
    assinatura_id: int = Field(foreign_key='assinatura.id')
    assinatura: Assinatura = Relationship()
    data_pagamento: date