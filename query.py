from sqlalchemy import create_engine

engine = create_engine('mysql://monolith:monolith@rchmontest01.fnoc.local/Events')

eventsConnect = engine.connect()
tid = eventsConnect.execute("SELECT tid FROM CircuitData where subscriber = 'KentuckyWired' limit 10").fetchall()
count = 0
for i in tid:
    print(f'Device {count} is {i}')
    count += 1
    print(type(i))
