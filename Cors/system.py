def gamesdel():
    print(" IMPORTING GAMES_DEL ")
    from Cors.Conf.Cherryofl.Modulsys.gamesdel.main import os

def dbdel():
    print(" IMPORTING DB_DEL")
    from Cors.Conf.Cherryofl.Modulsys.dbdel.main import os

def serverdel():
    print(" IMPORTING SERVER_DEL")
    from Cors.Conf.Cherryofl.Modulsys.serverdel.main import os
    
#=============================================================================================================

# Пример: from Cors.Conf.Cherryofl.Modulsys.(Имя модуля).(Имя файла) import os
# Живой пример: from Cors.Conf.Cherryofl.Modulsys.(Имя модуля > sloting).(Имя файла > main) import os
# Реальный пример: from Cors.Conf.Cherryofl.Modulsys.sloting.main import os

#=============================================================================================================
try:
    def slot():
        print(" IMPOTING SLOT ")
        from Cors.Conf.Cherryofl.Modulsys import os
except:
    print (" Отредактируйте system.py в директории Cors/system.py ")
#=============================================================================================================
