# Задание 8. Своя сеть: Redis

**Что делаем:** создаём пользовательскую сеть Docker и запускаем в ней
хранилище Redis.

**Зачем:** контейнеры в одной пользовательской сети видят друг друга
**по имени** — не нужно знать IP-адреса. Так связывают приложение и базу.

## Шаг 1. Создайте сеть

```bash
docker network create my-network
docker network ls
```

## Шаг 2. Запустите Redis в этой сети

```bash
docker run -d --name redis-server --network my-network redis
```

Обратите внимание: порт наружу (`-p`) мы НЕ пробрасываем — Redis нужен
только другим контейнерам, снаружи он не доступен. Это правильно
с точки зрения безопасности.

## Шаг 3. Проверьте, что Redis отвечает

Выполните команду redis-cli внутри контейнера:

```bash
docker exec -it redis-server redis-cli ping
```

Ожидаемый ответ: `PONG`.

## Шаг 4. Посмотрите на сеть изнутри

```bash
docker network inspect my-network
```

Найдите в JSON секцию `Containers` — там `redis-server` с его IP.

## Результат

**В отчёт:** `PONG` и IP-адрес redis-server из inspect.

> В следующем задании два Python-контейнера положат в Redis сообщение
> и прочитают его — по имени `redis-server`, без IP.
