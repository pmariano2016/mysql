from sqlalchemy import create_engine

engine = create_engine('mysql://monolith:monolith@rchmontest01.fnoc.local/Events')

eventsConnect = engine.connect()
tid = eventsConnect.execute("SELECT tid FROM CircuitData where subscriber = 'KentuckyWired' limit 10").fetchall()
print(tid)
