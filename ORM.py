from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_, and_

from eventsdb import CircuitDatum

Base = declarative_base()

session = sessionmaker()
engine = create_engine('mysql://monolith:monolith@rchmontest01.fnoc.local/Events')
engine_echo = create_engine('mysql://monolith:monolith@rchmontest01.fnoc.local/Events', echo=True)
session.configure(bind=engine)

connection_echo = engine_echo.connect()

my_session = session()
session_echo = sessionmaker(bind=engine_echo)()

print(my_session.query(CircuitDatum).first().Customer)
print(session_echo.query(CircuitDatum).first().Customer)

# Filter results
ky = my_session.query(CircuitDatum).filter(CircuitDatum.Subscriber == 'KentuckyWired').all()
# for i in ky:
# print(i)

# Like
like = my_session.query(CircuitDatum).filter(CircuitDatum.TID.like('%JN4300%')).all()
# contains

contains = my_session.query(CircuitDatum).filter(CircuitDatum.TID.contains('KYWDASHL017801JN4300')).all()
print(contains)

# Functions
# limit
limit = my_session.query(CircuitDatum).filter(CircuitDatum.TID.contains('KYWDASHL017801JN4300')).limit(4).all()
print(limit)

# Order By
order = my_session.query(CircuitDatum).filter(CircuitDatum.TID.contains('KYWDASHL017801JN4300')). \
    order_by(CircuitDatum.UniqueID).limit(4).all()
print(order)

orderDesc = my_session.query(CircuitDatum).filter(CircuitDatum.TID.contains('KYWDASHL')). \
    order_by(CircuitDatum.UniqueID.desc()).limit(4).all()
print(orderDesc)

# Conjunctions
# and
andConjun = my_session.query(CircuitDatum).filter(CircuitDatum.TID == 'KYWDASHL017801JN4300',
                                                  CircuitDatum.AID == 'UnknownAID').all()
print(andConjun)

# OR

ORC = my_session.query(CircuitDatum).filter(or_(CircuitDatum.TID == 'KYWDASHL017801JN4300',
                                                  CircuitDatum.TID == 'KY-PKV-Txt-2-911',)).filter(and_(CircuitDatum.AID == 'UnknownAID')).all()
print(ORC)