### Selecionar todos os registros

```bash
from sqlmodel import select
````


```bash
statement = select(ModelClass)
results = session.exec(statement).all()
````

### Filtrar registros

```bash
statement = select(ModelClass).where(ModelClass.campo == valor)
results = session.exec(statement).first()
````

### Métodos disponíveis após exec()

**.all()** Retorna todos os resultados

**.first()** Retorna primeiro resultado

**.one()** Retorna um resultado (erro se houver mais de um)

**.one_or_none()** Retorna um resultado ou None