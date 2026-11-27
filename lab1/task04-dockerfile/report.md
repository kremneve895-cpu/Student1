## Задание 5. Сборка и запуск собственного образа

### Ход работы

1. Перешёл в папку с Dockerfile:
    ```bash
    cd ~/Student1/docker-lab-students/lab1/task04-dockerfile
    ```

2. Запустил контейнер:
    ```bash
    docker run -d -p 8080:80 hello-docker
    ```
    Контейнер запустился с ID:
    ```
    <ID контейнера>
    ```

3. Проверил доступность:
    ```bash
    curl -s http://localhost:8080
    ```
    Получил ответ:
    ```
    Hello, Docker!
    ```

4. Пересобрал образ после изменения `app.py`:
    ```bash
    docker build -t hello-docker .
    ```
    Запустил обновлённый контейнер:
    ```bash
    docker run -d -p 8080:80 hello-docker
    ```
    Получил обновлённый ответ:
    ```
    Hello, Docker! Updated!
    ```

### Вывод
Образ успешно собран и запущен. При пересборке использовались кэшированные слои, кроме изменения в CMD.
