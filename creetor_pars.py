import re
import os
from lxml import etree
parser=etree.XMLParser(remove_comments=True,recover=True)#настройки парсера 
def lib(xmlFile,naim):#читаем файл
    lib=[]#создаем пустой словарь
    for i in xmlFile.iter():#заполняем словарь 
        if etree.QName(i.tag).localname==naim:
            for k in i.iterchildren():
                s=lib_chil(k)
                if s=="fiar":
                    return 'fiar'
        else:
            continue
    return lib#возвращаем
def lib_chil(chil):#создание словарей
    lib={}#создаем пустой словарь
    if len(chil) != 0 :#узнаём в теге есть ещо теги или только текст
        for child_root in chil.iterdescendants():#проходимся по всем тегам в нутри расматриваемого тега
            lib_elem=lib_chil(child_root)
            if type(lib_elem)==type(dict()):
                return 'fiar'
            elif lib_elem=="fiar":
                return 'fiar'
            else:
                lib[re.sub(r'(?<!^)(?=[A-Z])', '_',str(etree.QName(child_root.tag).localname) ).lower() ]=lib_elem#в писание в текущий словарь под ключом имя тега то что в нем
    else:#если в нутри нашего тега нету тегов
        return chil.text#передай текст тега
    return lib#верни список всех тегов всех

fails=[]#
fails=os.listdir("libreal")#получение списка всех файлов в библеотеке
with open ("wraiter","w") as wraiter:
    for i in fails:#обработка всех файлов
        with open("libreal/"+i) as fobj:#открытие файла
            pars=etree.parse(fobj,parser)
            naim = etree.QName(pars).localname
            s=lib(pars,naim)
            if s!="fiar":
                wraiter.write(str(s))