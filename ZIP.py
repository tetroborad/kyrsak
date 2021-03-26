#только дастоет конкретный файл из конкретной папки all_doc и переносит в папку либ
import os, zipfile ,shutil
for i in os.listdir("all_doc/"):
    for k in os.listdir("all_doc/"+i):
        zipFile = zipfile.ZipFile('all_doc/'+i+"/"+k)
        lis=zipFile.namelist()# получаем информацию о файлах и директориях
        for y in lis:
            pyt=zipFile.extract(y) # извлекаем отдельный файл из корня архива
            shutil.move(pyt,'libreal/'+y)
#zipFile.extractall() [grn]# извлекаем весь архив в текущую директорию
#zipFile.extractall('archive') [grn]# извлекаем весь архив в директорию archive[/grn]
zipFile.close()