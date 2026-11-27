## Задание 6. Тома: MySQL с постоянным хранилищем

### Ход работы

1. Создал том:
    docker volume create mysql-data

2. Проверил список томов:
    docker volume ls

    DRIVER    VOLUME NAME
    local     mysql-data

3. Запустил MySQL с подключённым томом:
    docker run -d \
      --name mysql-container \
      -e MYSQL_ROOT_PASSWORD=secret \
      -v mysql-data:/var/lib/mysql \
      mysql:5.7

4. Проверил, что контейнер работает:
    docker ps

5. Посмотрел последние строки логов:
    docker logs mysql-container | tail -8

    [Note] InnoDB: Buffer pool(s) load completed at 261124 14:52:26
    [Note] Event Scheduler: Loaded 0 events
    [Note] mysqld: ready for connections.
    Version: '5.7.44'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
    [Note] [Entrypoint]: Entrypoint script for MySQL Server 5.7.44-1.el7 started.
    [Note] [Entrypoint]: Switching to dedicated user 'mysql'

### Вывод

Том mysql-data успешно создан и подключён к /var/lib/mysql. Данные хранятся отдельно от контейнера. В логах видно, что MySQL готов к соединениям (ready for connections), значит, задание выполнено.
