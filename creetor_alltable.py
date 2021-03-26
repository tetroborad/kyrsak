import re
import os#для файлов
from lxml import etree#для парсинга xml
parser=etree.XMLParser(remove_comments=True,recover=True)
def lib(xmlFile):#читаем файл
    lib={}#создаем пустой словарь
    lib[xmlFile.getroot()]=lib_chil(xmlFile.getroot())#заполняем словарь 
    return lib#возвращаем
def lib_chil(chil):#создание словарей
    id=0
    last_child=None
    lib={}#создаем пустой словарь
    if len(chil.getchildren())!=0:#узнаём в теге есть ещо теги или только текст
        for child_root in chil.getchildren():#проходимся по всем тегам в нутри расматриваемого тега
            lib_elem=lib_chil(child_root)
            if last_child==etree.QName(child_root.tag).localname:
                id=id+1#получаем словарь того что в нутри тега
            lib[str(etree.QName(child_root.tag).localname)+str(id)]=lib_elem#в писание в текущий словарь под ключом имя тега то что в нем
            last_child=etree.QName(child_root.tag).localname
    else:#если в нутри нашего тега нету тегов
        return chil.text#передай текст тега
    return lib#верни список всех тегов всех 
def check_table(lib):
    try:
        first=True
        with open ("alltable.py") as wraiter: 
            s=wraiter.readlines()
            for key in lib.keys():
                for key_2 in lib[key].keys():
                    for  key_3 in lib[key][key_2].keys():
                        s.index('class '+key_3[:int(len(key_3)-1)]+"(Base):\n")
                        try:
                            #создать сущность и создатель
                            for atr in lib[key][key_2][key_3].keys():
                                atr_naim=re.sub(r'(?<!^)(?=[A-Z])', '_', atr[:int(len(atr)-1)]).lower() 
                                if lib[key][key_2][key_3][atr]=='false' or lib[key][key_2][key_3][atr]=='true':
                                    s.index("\t"+atr_naim+"=Column(Boolean)\n")
                                elif len(lib[key][key_2][key_3][atr].keys())>=2:
                                    s.index("\t"+atr_naim+"=Column(String,ForeignKey(''))\n")
                                elif first:
                                    s.index("\t"+atr_naim+"=Column(String,primary_key=True)\n")
                                    first=False
                                else:
                                    s.index("\t"+atr_naim+"=Column(String)\n")
                        except:
                            return False
                    break
                break   
    except:
        return True
def creat_table(lib):
    first=True
    with open ("alltable.py") as wraiter: 
        s=wraiter.readlines()
        for key in lib.keys():
            for key_2 in lib[key].keys():
                for  key_3 in lib[key][key_2].keys():
                    s.insert(s.index('class nsiBudget(Base):\n'),"class "+key_3[:int(len(key_3)-1)]+"(Base):\n\t__tablename__ = '"+key_3[:int(len(key_3)-1)]+"'\n")#создать сущность и создатель
                    s.insert(s.index('        return n\n')+1,"\telif name=='"+key_3[:int(len(key_3)-1)]+"':\n\t\tx = "+key_3[:int(len(key_3)-1)]+"()\n\t\treturn x\n")
                    for atr in lib[key][key_2][key_3].keys():
                        atr_naim=re.sub(r'(?<!^)(?=[A-Z])', '_', atr[:int(len(atr)-1)]).lower() 
                        if lib[key][key_2][key_3][atr]=='false' or lib[key][key_2][key_3][atr]=='true':
                            s.insert(s.index('class nsiBudget(Base):\n'),"\t"+atr_naim+"=Column(Boolean)\n")
                        elif type(lib[key][key_2][key_3][atr])==type(dict()):
                            s.insert(s.index('class nsiBudget(Base):\n'),"\t"+atr_naim+"=Column(String,ForeignKey(''))\n")
                        elif first:
                            s.insert(s.index('class nsiBudget(Base):\n'),"\t"+atr_naim+"=Column(String,primary_key=True)\n")
                            first=False
                        else:
                            s.insert(s.index('class nsiBudget(Base):\n'),"\t"+atr_naim+"=Column(String)\n")
                    break
                break
            break
    with open ("alltable.py","w") as wraiter:
        for i in s:
            wraiter.write(str(i))     
def main():
    parser=etree.XMLParser(remove_comments=True,recover=True)#настройки парсера
    fails=[]#
    fails=os.listdir("libreal")#получение списка всех файлов в библеотеке
    with open ("wraiter","w") as wraiter:
        for i in fails:#обработка всех файлов
            with open("libreal/"+i) as fobj:#открытие файла
                xml = etree.parse(fobj,parser)#парсинк из документа 
            t=lib(xml)
            s=check_table(t)
            if  s:
                creat_table(t)
                check_table(t)
            else :
                
                wraiter.write(str(i)+"\n")#надо запомнить и посмотреть док лично

        
if __name__ == "__main__":
    main()