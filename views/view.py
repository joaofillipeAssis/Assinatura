import __init__
from models.database import engine
from sqlmodel import Session
from datetime import date
from models.models import Assinatura

class AssinaturaService:
    def __init__ (self, engine):
        self.engine = engine
    
    def create (self, subscription: Assinatura):

        #automatizar manipulação da conexão com o banco de dados
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription

ss = AssinaturaService(engine)

assinatura = Assinatura(
    empresa= "netflix",
    site= "netflix.com.br",
    data_assinatura= date.today(),
    valor= 25
)

ss.create(assinatura)