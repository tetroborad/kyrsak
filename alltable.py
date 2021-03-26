from re import fullmatch 
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)
Base = declarative_base()
class nsiCalendarDay(Base):
    __tablename__ = 'nsiCalendarDay'
    start_date=Column(String,primary_key=True)
    end_date=Column(String)
    days=Column(String,ForeignKey(''))
class nsiEPDocType(Base):
    __tablename__ = 'nsiEPDocType'
    code=Column(String,primary_key=True)
    name=Column(String)
    object_name=Column(String)
    update_date=Column(String)
    is_actual=Column(Boolean)
class nsiPurchaseDocumentTypes(Base):
    __tablename__ = 'nsiPurchaseDocumentTypes'
    placing_way_code=Column(String,primary_key=True)
    placing_way_type=Column(String)
    placing_way_name=Column(String)
    actual=Column(Boolean)
    document_types=Column(String,ForeignKey(''))
class nsiAbandonedReason(Base):
    __tablename__ = 'nsiAbandonedReason'
    id=Column(String,primary_key=True)
    code=Column(String)
    name=Column(String)
    object_name=Column(String)
    type=Column(String)
    doc_type=Column(String,ForeignKey(''))
    placing_way=Column(String,ForeignKey(''))
    actual=Column(Boolean)
class nsiDeviationFactFoundation(Base):
    __tablename__ = 'nsiDeviationFactFoundation'
    code=Column(String,primary_key=True)
    name=Column(String)
    actual=Column(Boolean)
class nsiAuditActionSubject(Base):
    __tablename__ = 'nsiAuditActionSubject'
    id=Column(String,primary_key=True)
    name=Column(String)
    actual=Column(Boolean)
class nsiBudget(Base):
    __tablename__ = 'nsiBudget'
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
    elif name=='nsiAuditActionSubject':
        x = nsiAuditActionSubject()
        return x
    elif name=='nsiDeviationFactFoundation':
        x = nsiDeviationFactFoundation()
        return x
    elif name=='nsiAbandonedReason':
        x = nsiAbandonedReason()
        return x
    elif name=='nsiPurchaseDocumentTypes':
        x = nsiPurchaseDocumentTypes()
        return x
    elif name=='nsiEPDocType':
        x = nsiEPDocType()
        return x
    elif name=='nsiCalendarDay':
        x = nsiCalendarDay()
        return x
def creat_table_all():
    Base.metadata.create_all(engine)
def drop_table_all():
    Base.metadata.drop_all(engine)