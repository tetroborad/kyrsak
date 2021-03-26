import os#для файлов
import sqlalchemy#для работы с БД
from lxml import etree#для парсинга xml
engine = create_engine('postgresql://zakupki:zakupki@localhost:15432/zakupki', echo = True)#
meta = MetaData()#мета данные
Session = sessionmaker(bind = engine) #сесия
parser=etree.XMLParser(remove_comments=True,recover=True)#настройки парсера

def rid_lib(lib,naim):#читаем получившуюся библеотеку
    for book in lib:#проходимся по всем ключам
        if lib[dook] == dict:#если значение какогото ключа равны списку то сначала по этому списку надо сделать таблицу
           rid_lib(lib[book],book)#цитаем ту библеотеку
        print("создали тоблицу поменьше")#m=creare_essence(naim,lib)#создаеим сущность
        lib[book]=m#символ того что уже создана таблица и надо будет соиденить
    print("внес всё")#creat_essence(naim,lib)#соберание всех уже созданных таблиц в одну общую. ДОКУМЕНТ

def creat_essence(naim,attribute):#создание таблиц
     ll_essence =  q.fetchall()#получение из БД всех таблиц
    creat=False
    for table in all_essence:
        if table==naim:
            creat=True

def lib(xmlFile):#читаем файл
    lib={}#создаем пустой словарь
    lib[xmlFile.getroot()]=lib_chil(xmlFile.getroot())#заполняем словарь 
    return lib#возвращаем

def lib_chil(chil):#создание словарей
    lib={}#создаем пустой словарь
    if len(chil.getchildren())!=0 :#узнаём в теге есть ещо теги или только текст
        for child_root in chil:#проходимся по всем тегам в нутри расматриваемого тега
            lib_elem=lib_chil(child_root)#получаем словарь того что в нутри тега
            lib[etree.QName(child_root.tag).localname]=lib_elem#в писание в текущий словарь под ключом имя тега то что в нем
    else:#если в нутри нашего тега нету тегов
        return chil.text#передай текст тега
    return lib#верни список всех тегов всех 

fails=[]#
fails=os.listdir("training")#получение списка всех файлов в библеотеке
for i in fails:#обработка всех файлов
    with open("training/"+i) as fobj:#открытие файла
        xml = etree.parse(fobj,parser)#парсинк из документа 
    t=lib(xml)#приврощение распарсеного документа в словарь словарей
    print(t)
#    rid_lib(t,doc)#внисение в БД