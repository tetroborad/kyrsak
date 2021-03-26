#только дастоет конкретный файл из конкретной папки all_doc и переносит в папку либ
import os, zipfile ,shutil
zipFile = zipfile.ZipFile('all_doc/nsiAbandonedReason/nsiAbandonedReasonList_all_20210321000003_001.xml.zip')
lis=zipFile.namelist()# получаем информацию о файлах и директориях
for i in lis:
    pyt=zipFile.extract(i) # извлекаем отдельный файл из корня архива
shutil.move(pyt,'libreal/nsiAbandonedReasonList_all_20210321000003_001')
#zipFile.extractall() [grn]# извлекаем весь архив в текущую директорию
#zipFile.extractall('archive') [grn]# извлекаем весь архив в директорию archive[/grn]
zipFile.close()