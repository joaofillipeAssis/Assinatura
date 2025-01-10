import __init__
from models.database import engine
from sqlmodel import Session, select
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

    def list_all (self):
        with Session(self.engine) as session:
            #equivale a query SQL para busca no banco de dados
            statement = select(Assinatura)

            #executa o statement (query exibir todos os registros)
            results = session.exec(statement).all()
            return results

ss = AssinaturaService(engine)

"""
___ CREATE ___

assinatura = Assinatura(
    empresa= "prime",
    site= "prime.com.br",
    data_assinatura= date.today(),
    valor= 19.9
)

ss.create(assinatura)

"""
print(ss.list_all())