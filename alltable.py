from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)
Base = declarative_base()
class DocumentType(Base):
    __tablename__ = 'document_type'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
    structured = Column(Boolean)
    referenc=relationship('purchase_document_type',backref="DocumentType_referenc_PurchaseDocumentTypes")
class PurchaseDocumentTypes(Base):
    __tablename__ = 'purchase_document_type'
    placing_way_type = Column(String, primary_key=True)
    placing_way_name = Column(String)
    placing_way_code = Column(String)
    document_type_id = Column(String,ForeignKey(DocumentType.code))
    actual = Column(Boolean)
class EPDocType(Base):
    __tablename__ = 'e_p_doc_type'
    code = Column(String, primary_key=True)
    name = Column(String)
    object_name = Column(String)
    update_date = Column(String)
    is_actual = Column(Boolean)
class Budget(Base):
    __tablename__ = 'budget'
    code = Column(String, primary_key=True)
    name = Column(String)
    actual = Column(Boolean)
def creat_table(name): 
    if name=='Budget':
        n = Budget()
        return n

def creat_table_all():
    Base.metadata.create_all(engine)
def drop_table_all():
    Base.metadata.drop_all(engine)