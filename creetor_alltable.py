import os#для файлов
from lxml import etree#для парсинга xml
parser=etree.XMLParser(remove_comments=True,recover=True)#настройки парсера
def lib(xmlFile):#читаем файл
    lib={}#создаем пустой словарь
    lib[xmlFile.getroot()]=lib_chil(xmlFile.getroot())#заполняем словарь 
    return lib#возвращаем
def lib_chil(chil):#создание словарей
    id=0
    last_child=None
    lib={}#создаем пустой словарь
    if chil.getchildren() != ai_list :#узнаём в теге есть ещо теги или только текст
        for child_root in chil.getchildren():#проходимся по всем тегам в нутри расматриваемого тега
            lib_elem=lib_chil(child_root)
            if last_child==etree.QName(child_root.tag).localname:
                id=id+1#получаем словарь того что в нутри тега
            lib[str(etree.QName(child_root.tag).localname)+str(id)]=lib_elem#в писание в текущий словарь под ключом имя тега то что в нем
            last_child=etree.QName(child_root.tag).localname
    else:#если в нутри нашего тега нету тегов
        return chil.text#передай текст тега
    return lib#верни список всех тегов всех 
def creat_table(lib):
    with open ("wraiter") as wraiter: 
        for key in lib.keys():
            for key_2 in lib[key].keys():
                for  key_3 in lib[key][key_2].keys():
                    wraiter#создать сущность и создатель
                    for atr in lib[key][key_2][key_3].keys():
                        atr_naim=atr[:int(len(atr)-1)]
                        #создание атрибутов таблицы
                #выходы из всего этого пиздеца
                 
fails=[]#
fails=os.listdir("libreal")#получение списка всех файлов в библеотеке
for i in fails:#обработка всех файлов
    with open("libreal/"+i) as fobj:#открытие файла
        xml = etree.parse(fobj,parser)#парсинк из документа 
    t=lib(xml)