# Задание 6. Образ в Docker Hub

**Что делаем:** публикуем образ нашего веб-приложения в Docker Hub —
публичный реестр образов.

**Зачем:** собранный образ должен жить не только на вашей машине.
Реестр — «полка» для образов (как Artifactory, если проходили, — но
для docker-образов).

## Шаг 1. Аккаунт и вход

1. Зарегистрируйтесь на https://hub.docker.com (если ещё нет).
2. Войдите из терминала:

```bash
docker login
```

## Шаг 2. Пересоберите образ с правильным именем

Имя образа в Docker Hub обязано начинаться с вашего логина.
ВПИШИТЕ свой логин вместо `USERNAME`:

```bash
cd ../task04-compose-files
docker build -t USERNAME/myapp-web:latest .
docker images | grep myapp-web
```

## Шаг 3. Опубликуйте

```bash
docker push USERNAME/myapp-web:latest
```

Откройте страницу репозитория на hub.docker.com — образ там.

## Шаг 4. Проверка «на чистой машине»

Удалите локальный образ и запустите стек так, чтобы образ приехал
из Docker Hub:

```bash
docker compose down
docker rmi USERNAME/myapp-web:latest
```

В `docker-compose.yml` у сервиса `web` замените `build: .` на:

```yaml
    image: USERNAME/myapp-web:latest
```

и запустите:

```bash
docker compose up -d
curl http://localhost:5001
```

В логах pull видно, что образ скачался из реестра.

## Результат

**В отчёт:** вывод `docker push` и ответ на вопрос: чем `build: .`
отличается от `image: ...` в compose-файле?

> Нет аккаунта / не хочется регистрироваться — сделайте то же самое
> на локальном registry: это задание pro07.
