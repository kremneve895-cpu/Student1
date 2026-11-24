## Задание 5. Сборка и запуск собственного образа

### Ход работы

1. Перешёл в папку с Dockerfile:

    cd ~/Student1/docker-lab-students/lab1/task04-dockerfile

2. Собрал образ:

    docker build -t hello-docker .

3. Запустил контейнер:

    docker run -d -p 8080:80 hello-docker

    ID контейнера:

    b56c60ec23cdd6ab3928aca9735e148fe3633607abf1ab63a577ba2cb2ac5f46

4. Проверил ответ:

    curl -s http://localhost:8080

    Hello, Docker!

5. Изменил app.py на print("Hello, Docker! Updated!") и пересобрал образ:

    docker build -t hello-docker .

    Слои FROM python:3.8-slim и WORKDIR /app брались из кэша (CACHED),
    COPY и CMD пересоздались, так как изменился файл app.py.

### Вывод

Образ собран и запущен. При пересборке Docker берёт из кэша неизменённые
слои и пересоздаёт только те, что стоят после изменившихся инструкций.
