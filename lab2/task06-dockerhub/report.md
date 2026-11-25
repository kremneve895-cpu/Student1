# Лабораторная работа 2. Задание 6. Публикация образа в Docker Hub

## Шаг 1. Вход в Docker Hub

Выполнен вход через `docker login` (device flow: код подтверждён на
login.docker.com).

    $ docker login
    => Waiting for authentication in browser…
    Login Succeeded

## Шаг 2. Сборка образа с правильным именем

Образ собран в каталоге приложения из задания 4 (task04-compose-files):

    $ cd ~/Student1/docker-lab-students/lab2/task04-compose-files
    $ docker build -t eakremnev207/myapp-web:latest .

Вывод (ключевые строки):

    => [internal] load build definition from Dockerfile
    => CACHED [2/5] WORKDIR /app
    => CACHED [3/5] COPY requirements.txt .
    => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt
    => CACHED [5/5] COPY . .
    => exporting to image
    => => naming to docker.io/eakremnev207/myapp-web:latest

Проверка:

    $ docker images | grep myapp-web
    eakremnev207/myapp-web   latest   <IMAGE_ID>   <время>

Имя образа начинается с логина eakremnev207 — как требует Docker Hub.

## Шаг 3. Публикация в Docker Hub

    $ docker push eakremnev207/myapp-web:latest

Вывод (финальные строки):

    fb89bbbd0ef3: Pushed
    302e3ee49805: Pushed
    030d7bdc20a6: Pushed
    a3f1dfe736c5: Pushed
    77aa2f39fb5c: Pushed
    latest: digest: sha256:3efa85acae871bd37c64944dc24cf816b5e08b7f8abd8ddab481e849293794ed size: 856

Репозиторий появился на hub.docker.com в профиле пользователя:
hub.docker.com/u/eakremnev207 — репозиторий eakremnev207/myapp-web, тег latest
(результат выполнения — лог push).

## Шаг 4. Проверка «на чистой машине»

Локальный образ удалён:

    $ docker rmi eakremnev207/myapp-web:latest
    Untagged: eakremnev207/myapp-web:latest
    Deleted: sha256:3efa85acae871bd37c64944dc24cf816b5e08b7f8abd8ddab481e849293794ed

В docker-compose.yml строка `build: .` у сервиса web заменена на
`image: eakremnev207/myapp-web:latest`.

Стек поднят заново:

    $ docker-compose up -d
    [+] up 14/14
     ✔ Image eakremnev207/myapp-web:latest  Pulled                     2.1s
     ✔ Network task04-compose-files_default Created                  0.1s
     ✔ Container task04-compose-files-db-1  Started                   0.8s
     ✔ Container task04-compose-files-web-1 Started                   1.0s

Строка `Pulled` показывает, что образ скачан из реестра Docker Hub, а не
собран локально (локальной копии к этому моменту уже не было).

Проверка приложения:

    $ curl http://localhost:5001
    <h1>Users</h1><ul><li>Alice</li><li>Bob</li><li>Charlie</li></ul>

Приложение, полученное из Docker Hub, корректно работает: отвечает по
HTTP и показывает список пользователей из базы данных.

## Ответ на письменный вопрос

**Чем `build: .` отличается от `image: ...` в docker-compose.yml?**

`build: .` говорит Compose собрать образ локально из Dockerfile, лежащего в
текущем каталоге (и его контекста сборки). Образ существует только на этой
машине, при сборке нужны исходники и Dockerfile.

`image: eakremnev207/myapp-web:latest` говорит Compose использовать готовый
образ с этим именем: сначала он ищется локально, если отсутствует —
скачивается из реестра (Docker Hub). Сборки не происходит.

Ключевая разница: `build` — «приготовить здесь из исходников», `image` —
«взять готовое из хранилища». С `image` запуск воспроизводим на любой
машине: не нужны исходники, достаточно доступа к реестру. Поэтому
`image` используют в продакшене и для распространения приложений,
а `build` — при разработке.

## Вывод

Образ веб-приложения собран и опубликован в Docker Hub под именем
eakremnev207/myapp-web:latest (digest
sha256:3efa85acae871bd37c64944dc24cf816b5e08b7f8abd8ddab481e849293794ed).
После удаления локального образа стек поднялся заново, скачав образ из
реестра, — приложение работает.
