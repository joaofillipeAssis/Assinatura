from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
from datetime import date
from decimal import Decimal

class Assinatura(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

## Excluir execução por importação
if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
