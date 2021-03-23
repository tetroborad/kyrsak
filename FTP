from ftplib import FTP 
ftp = FTP('ftp.zakupki.gov.ru')
ftp.login('free','free')
ftp.cwd('/fcs_nsi/nsiBudget/') 
lis = ftp.retrlines('LIST')
for i in lis:
    with open("libreal/"+i, 'wb') as fobj:   
        ftp.retrbinary('RETR '+i, fobj.write) # Введите имя файла для загрузки  
ftp.quit() # Завершить FTP-соединение  