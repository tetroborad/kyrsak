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
def pars_e_p_doc_type(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiEPDocType"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['object_name']=i.find("{*}objectName").text
        dic['update_date']=i.find("{*}updateDate").text
        dic['is_actual']=i.find("{*}isActual").text
        lis.append(dic)
    return lis
def pars_purchase_document_types(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiPurchaseDocumentTypes"):
        dic={}
        taim=[]
        dic['placing_way_code']=i.find("{*}placingWayCode").text
        dic['placing_way_type']=i.find("{*}placingWayType").text
        dic['placing_way_name']=i.find("{*}placingWayName").text
        dic['actual']=i.find("{*}actual").text
        for k in i.getiterator("{*}documentType"):
            taim.append(k.find("{*}code").text)
        dic['document_types']=taim
        lis.append(dic)
    return lis
def pars_abandoned_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiAbandonedReason"):
        dic={}
        if i.find('{*}objectName')!=None:
            dic['id']=i.find("{*}id").text
            dic['code']=i.find("{*}code").text
            dic['name']=i.find("{*}name").text
            dic['object_name']=i.find("{*}objectName").text
            dic['type']=i.find("{*}type").text
            dic['doc_type_id']=i.find("{*}docType/{*}code").text
            dic['placing_way_id']=i.find("{*}placingWay/{*}code").text
            dic['actual']=i.find("{*}actual").text
            lis.append(dic)  
        else:
            dic['id']=i.find("{*}id").text
            dic['code']=i.find("{*}code").text
            dic['name']=i.find("{*}name").text
            dic['type']=i.find("{*}type").text
            dic['doc_type_id']=i.find("{*}docType/{*}code").text
            dic['placing_way_id']=i.find("{*}placingWay/{*}code").text
            lis.append(dic)  
    return lis
def pars_andit_action_subjects(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiAuditActionSubject"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_bank_guarantee_refusal615_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBankGuaranteeRefusal615Reason"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_bank_guarantee_refusal_reason(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBankGuaranteeRefusalReason"):
        dic={}
        dic['id']=i.find("{*}id").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
def pars_budget_list(fail):
    lis=[]
    for i in fail.getiterator("{*}nsiBudget"):
        dic={}
        dic['code']=i.find("{*}code").text
        dic['name']=i.find("{*}name").text
        dic['actual']=i.find("{*}actual").text
        lis.append(dic)
    return lis
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
    return pars_bank_guarantee_refusal615_reason(pars)

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
