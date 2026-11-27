## Задание 9. Python-клиенты для Redis

### Ход работы

1. Скрипты уже содержали имя хоста redis-server:
    import redis
    r = redis.Redis(host="redis-server", port=6379)

2. Запустил писателя:
    docker run --rm --network my-network \
      -v $(pwd)/set_message.py:/set_message.py \
      python:3.8-slim bash -c "pip install -q redis && python /set_message.py"

    Вывод: Message set in Redis

3. Запустил читателя:
    docker run --rm --network my-network \
      -v $(pwd)/get_message.py:/get_message.py \
      python:3.8-slim bash -c "pip install -q redis && python /get_message.py"

    Вывод: Message from Redis: Hello from Python

### Почему в скриптах имя redis-server, а не IP-адрес?

Контейнеры в одной пользовательской сети Docker могут обращаться
друг к другу по имени контейнера. Это удобно и надёжно: IP-адрес
контейнера может измениться при его пересоздании (мы видели это в
задании 7: контейнер удалили и создали новый), а имя redis-server
останется тем же — скрипты при этом не придётся менять.

Имя разрешает встроенный DNS-сервер Docker: внутри контейнера он
доступен по адресу 127.0.0.11 и сопоставляет имена контейнеров
(заданные через --name) их текущим IP-адресам. Такая резолюция имён
работает только в пользовательских сетях — поэтому нам и была нужна
my-network из задания 8.

### Вывод

Два отдельных контейнера на чистом python:3.8-slim успешно
взаимодействуют через Redis: один записал в него сообщение
"Hello from Python", второй прочитал его — обратившись к серверу
по имени redis-server, без знания IP-адреса. Имя разрешил
встроенный DNS-сервер Docker внутри пользовательской сети
my-network.
