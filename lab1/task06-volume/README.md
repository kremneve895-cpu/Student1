# Задание 6. Тома: MySQL с постоянным хранилищем

**Что делаем:** запускаем базу данных MySQL с томом, чтобы данные
жили отдельно от контейнера.

**Зачем:** контейнер — временный: удалил — и всё внутри пропало.
Том (volume) хранит данные на диске Docker'а независимо от контейнера.

## Шаг 1. Создайте том

```bash
docker volume create mysql-data
docker volume ls
```

## Шаг 2. Запустите MySQL с подключённым томом

```bash
docker run -d \
  --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=secret \
  -v mysql-data:/var/lib/mysql \
  mysql:5.7
```

Разбор:
- `-e MYSQL_ROOT_PASSWORD=secret` — переменная окружения: пароль root в MySQL;
- `-v mysql-data:/var/lib/mysql` — том `mysql-data` подключён в каталог,
  где MySQL хранит данные.

## Шаг 3. Проверьте, что контейнер жив

```bash
docker ps
docker logs mysql-container | tail -5
```

В логах должно быть `ready for connections`.

## Результат

**В отчёт:** вывод `docker volume ls` и последние строки логов.

> Базу создадим в следующем задании — и проверим, что она переживёт
> удаление контейнера.
