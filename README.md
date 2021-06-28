# Шаги для выполнения задания
Установить VirtualBox и поставить на него Ubuntu 18.04.5 TLS 
Добавить репозиторий Greenplum в систему на VM 
Установить последнию версию Greenplum
Настроить файл gpinitsystem_singlenode по пути $GPHOME/docs/cli_help/gpconfigs/ : в нем установить переменные MACHINE_LIST_FILE, declare -a DATA_DIRECTORY, MASTER_HOSTNAME, MASTER_DIRECTORY
Стартануть кластер используя конфиг-файл gpinitsystem_singlenode 
Поставить в PyCharm плагины : flask, flask-sqlalchemy, sqlalchemy, pip 
Поставить в PyCharm модуль : psycopg2
Развернуть приложение на flask и добавть POST запрос : 
    name = request.form["name"]
    agreement = request.form["agreement"]

    db.session.add(Client(name, agreement))
    db.session.commit()
