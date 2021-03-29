import re
from datetime import datetime
taim=datetime.now()
import alltable
import os#для файлов
from lxml import etree#для парсинга xml
from sqlalchemy import *#для работы с БД
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = False)#
meta = MetaData()#мета данные
Session = sessionmaker(bind = engine) #создания класа сесии
s=Session()#образец класса сесия

parser=etree.XMLParser(remove_comments=True,recover=True)#настройки парсера 
#alltable.creat_table_all()
def lib(xmlFile,naim):#читаем файл
    lib=[]#создаем пустой словарь
    for i in xmlFile.iter():#заполняем словарь 
        if etree.QName(i.tag).localname==naim:
            for k in i.iterchildren():
                lib.append(lib_chil(k))
        else:
            continue
    return lib#возвращаем
def lib_chil(chil):#создание словарей
    lib={}#создаем пустой словарь
    if len(chil) != 0 :#узнаём в теге есть ещо теги или только текст
        for child_root in chil.iterdescendants():#проходимся по всем тегам в нутри расматриваемого тега
            lib_elem=lib_chil(child_root)
            if type(lib_elem)==type(dict()):
                for i in lib_elem.values():
                    lib[re.sub(r'(?<!^)(?=[A-Z])', '_',str(etree.QName(child_root.tag).localname) ).lower() ]=i
                    break
            else:
                lib[re.sub(r'(?<!^)(?=[A-Z])', '_',str(etree.QName(child_root.tag).localname) ).lower() ]=lib_elem#в писание в текущий словарь под ключом имя тега то что в нем
    else:#если в нутри нашего тега нету тегов
        return chil.text#передай текст тега
    return lib#верни список всех тегов всех

# parsed_data = [
#     {
#         'id': 'qweasdzxc',
#         'name': 'qweqweqwe',
#         'actual': True
#     }
# ]

#parsed_data = [
#    {
#        'id': 'qwe',
#        'code': 'qwe',
#        'name': 'qwe',
#        'objectName': 'qwe',
#        'type': 'qwe',
#        'doc_type_code': 'IZT',
#        'placing_way_code': 'ZKKP20',
#        'actual': True
#
#    },
#    ....
    
#]

#def parse_abondoned_reason(xml_file):
#    res = []
#    for tag in xml_file.find_all('nsiAuditActionSubject'):
#        res.append({
#            'id': tag.find('id').text,
#            'name': tag.find('name').text,
#            'actual': {'true': True, 'false': False}[tag.find('actual').text]
#        })
#    return res

#def import_objects(lib, model):
#    for data in lib:
#        obj = model(**data)
#        session.add(obj)
#    session.commit()

#import_objects(parsed_data, nsiAuditActionSubject)

def concrete_bazz_1(lib):
    for key in lib.keys():
        for key_2 in lib[key].keys():
            for  key_3 in lib[key][key_2].keys():
                if lib[key][key_2][key_3][actual]=='true':
                    ins=alltable.nsiAuditActionSubject(id=lib[key][key_2][key_3][id],name=lib[key][key_2][key_3][name],actual=True)
                else:
                    ins=alltable.nsiAuditActionSubject(id=lib[key][key_2][key_3][id],name=lib[key][key_2][key_3][name],actual=False)
                s.add(ins)
                s.commit() 
def concrete_bazz_2(lib):
    for key in lib.keys():
        for key_2 in lib[key].keys():
            for  key_3 in lib[key][key_2].keys():
                if lib[key][key_2][key_3][actual]=='true':
                    ins=alltable.nsiDeviationFactFoundation(code=lib[key][key_2][key_3][code],name=lib[key][key_2][key_3][name],actual=True)
                else:
                    ins=alltable.nsiDeviationFactFoundation(code=lib[key][key_2][key_3][code],name=lib[key][key_2][key_3][name],actual=False)
                s.add(ins)
                s.commit() 
def dazz (fail,parser):
    pars=etree.parse(fail,parser)
    naim = fail.name[fail.name.find('/')+1:fail.name.find('_')]
    return lib(pars,naim)

fails=[]#
fails=os.listdir("libreal")#получение списка всех файлов в библеотеке
with open ("wraiter","w") as wraiter:
    for i in fails:#обработка всех файлов
        with open("libreal/"+i) as fobj:#открытие файла
             t=dazz(fobj,parser)#парсинк из документа 
        wraiter.writelines(str(t))
       # if i[4]=='A':
       #     concrete_bazz_1(t)
       # else:
       #     concrete_bazz_2(t)
       # #t=dazz(t)-универсальный парсер. да да зачем он нам он всевото уменьшит работу и решит проблемы
#    for row in s.query(alltable.nsiDeviationFactFoundation).all():
#        wraiter.writelines(str(row.code)+" "+str(row.name)+" "+str(row.actual)+"\n")
#    for row in s.query(alltable.nsiAuditActionSubject).all():
#        wraiter.writelines(str(row.code)+" "+str(row.name)+" "+str(row.actual)+"\n")
#print(datetime.now()-taim)
