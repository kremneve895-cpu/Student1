## Задание 3. Фоновый контейнер, stop и rm

### Ход работы

1. Запустил nginx в фоне:

    docker run -d --name web -p 8080:80 nginx

    Флаги: -d — фоновый режим, --name web — своё имя контейнера,
    -p 8080:80 — порт 80 контейнера проброшен на порт 8080 хоста.
    Контейнеру присвоен ID 94c749d51421.

2. Проверил список работающих контейнеров:

    $ docker ps
    CONTAINER ID   IMAGE                                                   COMMAND                  CREATED          STATUS          PORTS                                            NAMES
    94c749d51421   nginx                                                   "/docker-entrypoint.…"   12 seconds ago   Up 11 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp          web
    34ec55983d59   releases-docker.jfrog.io/jfrog/artifactory-jcr:latest   "/usr/local/bin/fips…"   5 days ago       Up 19 seconds   0.0.0.0:8081-8082->8081-8082/tcp, [::]:8081-8082->8081-8082/tcp  artifactory
    c28fbfff6420   postgres:16                                             "docker-entrypoint.s…"   5 days ago       Up 19 seconds   5432/tcp                                          postgres

    Контейнер web запущен, порт 8080 на хосте связан с портом 80 контейнера.

3. Проверил доступность сайта:

    $ curl -s http://localhost:8080 | head -20
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
    html { color-scheme: light dark; }
    body { width: 35em; margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif; }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>

    nginx отдаёт свою стандартную стартовую страницу.

4. Остановил контейнер:

    $ docker stop web
    web

    Docker вернул имя остановленного контейнера. После этого web исчез
    из списка docker ps (остались только artifactory и postgres).

5. Проверил, что сайт больше не отвечает:

    $ curl http://localhost:8080
    curl: (7) Failed to connect to localhost port 8080 after 0 ms: Could not connect to server

    Соединение не устанавливается: главный процесс контейнера остановлен,
    порт 8080 на хосте больше никто не слушает.

6. Удалил контейнер:

    $ docker rm web
    web

    $ docker ps -a
    (вывод показан ниже)
    CONTAINER ID   IMAGE                                                   COMMAND                  CREATED             STATUS                         PORTS                                                             NAMES
    00a4fbbee32c   ubuntu                                                  "bash"                   About an hour ago   Exited (0) About an hour ago                                                                     practical_moser
    803b30b2ddec   hello-world                                             "/hello"                 3 hours ago         Exited (0) 3 hours ago                                                                           admiring_ritchie
    5b089b221825   ubuntu                                                  "sleep infinity"         4 hours ago         Exited (255) 2 hours ago       0.0.0.0:2222->22/tcp, [::]:2222->22/tcp                           ubuntu-ssh
    6ab23e00467c   redis                                                   "docker-entrypoint.s…"   20 hours ago        Exited (0) 20 hours ago                                                                          redis-server
    47408011f91e   mysql:5.7                                               "docker-entrypoint.s…"   23 hours ago        Exited (0) 22 hours ago                                                                          mysql-lab
    f7f533312fd2   nginx                                                   "/docker-entrypoint.…"   5 days ago          Exited (0) 5 days ago                                                                            charming_khayyam
    34ec55983d59   releases-docker.jfrog.io/jfrog/artifactory-jcr:latest   "/usr/local/bin/fips…"   5 days ago          Up 2 minutes                   0.0.0.0:8081-8082->8081-8082/tcp, [::]:8081-8082->8081-8082/tcp   artifactory
    c28fbfff6420   postgres:16                                             "docker-entrypoint.s…"   5 days ago          Up 2 minutes                   5432/tcp                                                          postgres
    38ddb610079c   postgres:15-alpine                                      "docker-entrypoint.s…"   5 days ago          Exited (0) 5 days ago                                                                            artifactory-postgres

    Контейнера web в списке больше нет: docker rm удалил его полностью,
    при этом остальные контейнеры и образ nginx не затронуты.

### Ответ на вопрос задания

docker stop останавливает главный процесс контейнера, но сам контейнер
остаётся: его файловая система, данные и настройки сохраняются, статус
становится Exited. Такой контейнер можно запустить заново командой
docker start web.

docker rm полностью удаляет контейнер: исчезают файловая система, логи,
настройки и имя. Восстановить его нельзя — можно только создать новый.

После stop, но до rm остаются: сам контейнер (виден в docker ps -a),
все изменения внутри его файловой системы и привязка портов. После rm
всё это исчезает, имя web и порт 8080 освобождаются.

Ни stop, ни rm не затрагивают образ: nginx остаётся в docker images,
и из него можно создать сколько угодно новых контейнеров.
