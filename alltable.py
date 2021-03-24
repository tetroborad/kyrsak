from re import fullmatch 
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)
Base = declarative_base()
class nsiBudget(Base):
    __tablename__ = 'nsiBudget'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
class xdf (Base):
    __tablename__ = 'xdf'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
def creat_table(name): 
    reg=r'\w+[^\d]'
    while not fullmatch(reg,name) :
        name=name[:int(len(name)-1)]
    if name=='nsiBudget':
        n = nsiBudget()
        return n
def creat_table_all():
    Base.metadata.create_all(engine)
def drop_table_all():
    Base.metadata.drop_all(engine)