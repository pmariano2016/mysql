# coding: utf-8
from sqlalchemy import CHAR, Column, Date, Float, Index, String, Table, Text, VARCHAR, text
from sqlalchemy.dialects.mysql.types import TINYINT, BIGINT, INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CircuitDatum(Base):
    __tablename__ = 'CircuitData'
    __table_args__ = (
        Index('tidaid', 'TID', 'AID', unique=True),
    )

    UniqueID = Column(INTEGER(10), primary_key=True)
    Customer = Column(String(64))
    Subscriber = Column(String(64))
    TID = Column(CHAR(64), index=True)
    AID = Column(String(64), index=True)
    CircuitID = Column(String(64))
    DateEntered = Column(BIGINT(20))
    AccountID = Column(String(32))
    Action = Column(String(16))
    IPAddress = Column(String(20))
    Urgency = Column(String(64), index=True)
    Active = Column(INTEGER(11), server_default=text("'1'"))
    EquipmentType = Column(String(36))
    GPSLoc = Column(String(36), nullable=False, server_default=text("'0'"))
    UUID = Column(String(36), nullable=False, index=True, server_default=text("'0'"))
    LogUUID = Column(String(36), nullable=False, server_default=text("'0'"))
    VirUUID = Column(String(36))
    DeptID = Column(String(32), server_default=text("'0'"))
    DisplayName = Column(String(128))
    Smoothing = Column(INTEGER(10), nullable=False, server_default=text("'1'"))


def _abort_ro():
    print("Session in Read-Only Mode!")
    return


def db_session_setup(constring, readonly=True):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # set up the database connection:
    engine = create_engine(constring)
    if readonly:
        engine.execute('set transaction read only')
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    if readonly:
        session.commit = _abort_ro
    return session



