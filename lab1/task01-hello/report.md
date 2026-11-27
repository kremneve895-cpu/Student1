# Отчет по заданию 1 (task01-hello)

## Шаг 1. Проверка Docker

docker version: Client и Server 29.1.3, API 1.52
docker-compose version: v5.7.0

## Шаг 2. Запуск hello-world

docker run hello-world: вывел Hello from Docker!,
образ автоматически скачан из Docker Hub.

## Шаг 3. Ответы на вопросы

1. Образа hello-world не было локально, Docker сам
   скачал его из Docker Hub.
2. Из публичного реестра Docker Hub (docker.io).
3. Контейнер завершился сразу после вывода сообщения.
   docker ps - только работающие контейнеры.
   docker ps -a - все, включая остановленные;
   hello-world виден со статусом Exited (0).

## Шаг 4. Локальное хранилище образов

docker images: hello-world:latest, ID 1e4c05b897a7,
размер 9.49kB. Образ хранится локально.

## Вывод

Docker работает. Образ hello-world скачан из Docker Hub,
контейнер запущен и завершился с кодом 0. Разница между
docker ps и docker ps -a проверена на практике.
