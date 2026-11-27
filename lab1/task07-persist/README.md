# Задание 7. Данные переживают контейнер

**Что делаем:** создаём базу в MySQL, **удаляем контейнер**, запускаем
новый — и проверяем, что база на месте.

## Шаг 1. Создайте базу данных

Подключитесь к MySQL внутри контейнера (пароль — `secret`):

```bash
docker exec -it mysql-container mysql -uroot -p
```

Внутри MySQL:

```sql
CREATE DATABASE testdb;
SHOW DATABASES;
EXIT;
```

## Шаг 2. Удалите контейнер

```bash
docker rm -f mysql-container
docker ps -a
```

Контейнера больше нет. Если бы том не был подключён, данные пропали бы
вместе с ним.

## Шаг 3. Запустите новый контейнер с тем же томом

```bash
docker run -d \
  --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=secret \
  -v mysql-data:/var/lib/mysql \
  mysql:5.7
```

## Шаг 4. Проверьте, что база сохранилась

```bash
docker exec -it mysql-container mysql -uroot -p
```

```sql
SHOW DATABASES;
```

`testdb` на месте, хотя контейнер — совершенно новый.

## Результат

**В отчёт:** вывод `SHOW DATABASES` после пересоздания контейнера
и ответ на вопрос: где физически лежат данные (подсказка:
`docker volume inspect mysql-data`)?
