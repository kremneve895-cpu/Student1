## Задание 7. Данные переживают контейнер

### Ход работы

1. Создал базу данных в MySQL:
    docker exec -it mysql-container mysql -uroot -p

    CREATE DATABASE testdb;
    SHOW DATABASES;
    EXIT;

    База testdb появилась в списке.

2. Удалил контейнер:
    docker rm -f mysql-container
    docker ps -a

    Контейнера mysql-container больше нет. Том mysql-data остался
    (проверено командой docker volume ls).

3. Запустил новый контейнер с тем же томом:
    docker run -d \
      --name mysql-container \
      -e MYSQL_ROOT_PASSWORD=secret \
      -v mysql-data:/var/lib/mysql \
      mysql:5.7

4. Проверил, что база сохранена:
    docker exec -it mysql-container mysql -uroot -p

    SHOW DATABASES;

    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | sys                |
    | testdb             |
    +--------------------+

    База testdb на месте, хотя контейнер — совершенно новый.

5. Проверил, где физически находятся данные:
    docker volume inspect mysql-data

    "Mountpoint": "/var/lib/docker/volumes/mysql-data/_data"

### Вывод

База данных testdb пережила удаление контейнера: новый контейнер,
запущенный с тем же томом mysql-data, сразу увидел её в списке баз.
Физически данные хранятся не внутри контейнера, а на диске хоста —
в каталоге /var/lib/docker/volumes/mysql-data/_data (этот путь
показывает Mountpoint в выводе docker volume inspect). Контейнер
содержит только саму СУБД, а данные живут в томе, поэтому их можно
сохранять между перезапусками и заменами контейнера.
