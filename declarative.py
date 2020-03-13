from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy import func, and_, not_

import eventsdb as ev

engine = create_engine('mysql://monolith:monolith@pri-monpres-01.fnoc.local/Events')


my_session = ev.db_session_setup(constring=engine)
my_session.query(ev.CircuitDatum).first()
