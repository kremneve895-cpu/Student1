## Задание 8. Своя сеть: Redis

### Ход работы

1. Создал пользовательскую сеть:
    docker network create my-network
    docker network ls

    В списке сетей появилась my-network (драйвер bridge).

2. Запустил Redis в этой сети:
    docker run -d --name redis-server --network my-network redis

    Порт наружу (-p) не пробрасывал: Redis нужен только другим
    контейнерам внутри сети, снаружи он недоступен.

3. Проверил, что Redis отвечает:
    docker exec -it redis-server redis-cli ping

    PONG

4. Посмотрел на сеть изнутри:
    docker network inspect my-network

    Сеть создана с подсетью 172.19.0.0/16 (шлюз 172.19.0.1).
    В секции Containers указан redis-server с IP-адресом:
    IPv4Address: 172.19.0.2/16

### Вывод

Пользовательская сеть my-network создана, Redis запущен внутри неё
и отвечает на ping (PONG). Сетью управляет драйвер bridge, Docker
сам выделил подсеть 172.19.0.0/16 и назначил контейнеру IP
(172.19.0.2). Порт наружу не открыт — Redis доступен только
контейнерам этой сети, что правильно с точки зрения безопасности.
В следующем задании Python-контейнеры будут обращаться к Redis
по имени redis-server, без указания IP.
