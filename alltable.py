from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)
Base = declarative_base()

class OKEI(Base):
    __tablename__ = 'OKEI'
    code = Column(String, primary_key=True)
    full_name = Column(String)
    local_name = Column(String)
    actual = Column(Boolean)
class Currency(Base):
    __tablename__ = 'Currency'
    code = Column(String, primary_key=True)
    full_name = Column(String)
    local_name = Column(String)
    actual = Column(Boolean)
class KVR(Base):
    __tablename__ = 'KVR'
    code = Column(String, primary_key=True)
    full_name = Column(String)
    local_name = Column(String)
    actual = Column(Boolean)
class DrugOKEI(Base):
    __tablename__ = 'DrugOKEI'
    code = Column(String, primary_key=True)
    full_name = Column(String)
    local_name = Column(String)
    actual = Column(Boolean)
class WorldTimeZone(Base):
    __tablename__ = 'WorldTimeZone'
    name = Column(String, primary_key=True)
    difference_time = Column(String)
    is_actual = Column(Boolean)
class CommissionRole(Base):
    __tablename__ = 'CommissionRole'
    id = Column(String, primary_key=True)
    code = Column(String)
    name = Column(String)
    order = Column(String)
    right_vote = Column(String)
    is_actual = Column(Boolean)
class ClosedEPCases(Base):
    __tablename__ = 'ClosedEPCases'
    code = Column(String, primary_key=True)
    name = Column(String)
    update_date = Column(String)
    is_actual = Column(Boolean)
class ChangePriceFoundation(Base):
    __tablename__ = 'ChangePriceFoundation'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
class Budget(Base):
    __tablename__ = 'Budget'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
class BankGuaranteeRefusalReason(Base):
    __tablename__ = 'BankGuaranteeRefusalReason'
    id = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
class AuditActionSubject(Base):
    __tablename__ = 'AuditActionSubject'
    id = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
class AbandonedReason(Base):
    __tablename__ = 'AbandonedReason'
    id = Column(String, primary_key=True)
    code = Column(String)
    name = Column(String)
    object_name = Column(String)
    type = Column(String)    
    doc_type_id = Column(String)
    placing_way_id = Column(String)
    actual = Column(Boolean)
class DocumentType(Base):
    __tablename__ = 'DocumentType'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
    structured = Column(Boolean)
    def __init__(self, dic):
        for key in dic.keys():
            if dic[key]=="true":
                dic[key]=True
            elif dic[key]=="false":
                dic[key]=False
        self.name = dic["name"]
        self.code = dic["code"]
        self.actual = dic["actual"]
        self.structured = dic["structured"]
class PurchaseDocumentTypes(Base):
    __tablename__ = 'PurchaseDocumentTypes'
    placing_way_type = Column(String, primary_key=True)
    placing_way_name = Column(String)
    placing_way_code = Column(String)
    document_type_id = Column(String,ForeignKey(DocumentType.code))
    actual = Column(Boolean)
    def __init__(self, dic):
        for key in dic.keys():
            if dic[key]=="true":
                dic[key]=True
            elif dic[key]=="false":
                dic[key]=False
        self.placing_way_type = dic["placing_way_type"]
        self.placing_way_name = dic["placing_way_name"]
        self.placing_way_code = dic["placing_way_code"]
        self.document_type_id = dic["document_type_id"]
        self.actual = dic["actual"]
class EPDocType(Base):
    __tablename__ = 'EPDocType'
    code = Column(String, primary_key=True)
    name = Column(String)
    object_name = Column(String)
    update_date = Column(String)
    is_actual = Column(Boolean)
def creat_table(name,dic): 
    if name=='dudget':
        n = Budget(dic)
        return n
    elif name=='purchase_document_types':
        n = PurchaseDocumentTypes(dic)
        return n
    elif name=='document_type_id':
        n = DocumentType(dic)
        return n

def creat_table_all():
    Base.metadata.create_all(engine)
def drop_table_all():
    Base.metadata.drop_all(engine)