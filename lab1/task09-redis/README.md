# Задание 9. Python-клиенты к Redis

**Что делаем:** два отдельных контейнера общаются через Redis:
один кладёт значение, другой читает.

## Шаг 1. Скрипт-писатель уже лежит в папке

Откройте `set_message.py` — ВПИШИТЕ имя хоста Redis
(то, что вы давали контейнеру через `--name` в задании 8).

## Шаг 2. Запустите писателя

Важно: выполняйте из папки задания внутри домашнего каталога
(не из `/tmp` — на macOS с colima каталог `/tmp` не пробрасывается
в Docker, и файл внутри контейнера окажется пустым).

```bash
docker run --rm --network my-network \
  -v $(pwd)/set_message.py:/set_message.py \
  python:3.8-slim bash -c "pip install -q redis && python /set_message.py"
```

Разбор:
- `--rm` — удалить контейнер после завершения (он разовый);
- `-v $(pwd)/set_message.py:/set_message.py` — пробросить файл с хоста
  внутрь контейнера;
- `bash -c "pip install redis && python ..."` — в чистом образе нет
  библиотеки redis, ставим на лету (в вебинаре эта часть команды
  потерялась — без неё будет ModuleNotFoundError).

Должно напечатать `Message set in Redis`.

## Шаг 3. Скрипт-читатель

Откройте `get_message.py`, ВПИШИТЕ тот же хост. Запустите:

```bash
docker run --rm --network my-network \
  -v $(pwd)/get_message.py:/get_message.py \
  python:3.8-slim bash -c "pip install -q redis && python /get_message.py"
```

Должно напечатать `Message from Redis: Hello from Python`.

## Результат

**В отчёт:** вывод читателя и ответ на вопрос: почему в скриптах
указано имя `redis-server`, а не IP-адрес, и кто это имя разрешает?
