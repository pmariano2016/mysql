from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

session = sessionmaker()
engine = create_engine('mysql://monolith:monolith@rchmontest01.fnoc.local/Events')
session.configure(bind=engine)
my_session = session()

sql = "SELECT tid, Account FROM CircuitData limit 10"

sqlObj = my_session.execute(sql)
print(sqlObj)


