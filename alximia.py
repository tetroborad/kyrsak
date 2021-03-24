from alltable import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)
Session = sessionmaker(bind = engine) 
session = Session()


nit_live=False
#meta.create_all(engine)
#conn = engine.connect()
#mapper(Stydent, stydent)
#mapper(Zakpki, zakpki) 
#stmt=Stydent(22,'vladimer',False)
#stmt=stydent.insert().values(ear=19,name='Ivana',liev=True)
#conn.execute(stmt)
#s = stydent.select()
#print(conn.execute(s))
creat_table_all()
vasia_stydent = Stydent()
zina_stydent = Stydent({"zina",19,True})
session.add(vasia_stydent)
session.add(zina_stydent)
for i in session.query(Stydent).all():
    print(i.name,i.ear,i.liev)
session.commit()





