# Лабораторная работа 2. Задание 5. Запуск стека через Compose

## Цель
Поднять стек из двух сервисов (web + PostgreSQL) одной командой
docker compose up и убедиться, что приложение работает.

## Шаг 1. Запуск стека
Команда (в моей системе compose вызывается как docker-compose):

    docker-compose up -d --build

Вывод:
    [+] up 22/22
     ✔ Image postgres:13                    Pulled      50.0s
     ✔ Image task04-compose-files-web       Built       67.6s
     ✔ Network task04-compose-files_default Created     0.1s
     ✔ Volume task04-compose-files_pgdata   Created     0.0s
     ✔ Container task04-compose-files-db-1  Started     4.5s
     ✔ Container task04-compose-files-web-1 Started     2.7s

Флаги: up -d поднимает все сервисы в фоне, --build пересобирает образ web.

## Шаг 2. Проверка статуса сервисов

    $ docker-compose ps
    NAME                         IMAGE                      SERVICE   STATUS         PORTS
    task04-compose-files-db-1    postgres:13                db        Up 39 seconds  5432/tcp
    task04-compose-files-web-1   task04-compose-files-web   web       Up 37 seconds  0.0.0.0:5001->5001/tcp

Оба контейнера в статусе Up, порт 5001 проброшен на хост.

## Шаг 3. Проверка приложения

    $ curl http://localhost:5001
    <h1>Users</h1><ul><li>Alice</li><li>Bob</li><li>Charlie</li></ul>

Приложение вернуло HTML со списком пользователей, ошибки 500 не возникло.

## Шаг 4. Логи сервисов

    $ docker-compose logs web | tail -5

    $ docker-compose logs db | tail -5

## Шаг 5. Остановка стека

    $ docker-compose down
    $ docker-compose ps
    NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

    $ docker volume ls
    DRIVER    VOLUME NAME
    local     task04-compose-files_pgdata

После down контейнеры и сеть удалены, том pgdata остался — данные
сохраняются между запусками стека.

## Ответ на письменный вопрос
Вопрос: что будет с таблицей users, если выполнить docker compose down -v?

Ответ: флаг -v удаляет вместе с контейнерами и сетью именованные тома,
объявленные в docker-compose.yml (том pgdata для /var/lib/postgresql/data).
Данные таблицы users хранятся не в контейнере, а в этом томе — это
подтверждено в задании 7 лабораторной 1: контейнер MySQL удаляли и создавали
заново, а база testdb сохранилась, потому что жила в томе mysql-data.

Поэтому docker compose down -v полностью удалит таблицу users вместе с томом.
При следующем up создастся новый пустой том, PostgreSQL выполнит первичную
инициализацию и заново прогонит init.sql — восстановятся только структура
таблицы и стартовые записи Alice, Bob, Charlie. Все данные, добавленные
после инициализации, будут потеряны.

## Вывод
Стек из двух контейнеров поднят одной командой. Приложение работает
на порту 5001. Обычный down сохраняет данные в томе, down -v удаляет
их вместе с томом.
