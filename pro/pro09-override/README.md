# Pro 9. Compose override: dev и prod

**Цель:** одна кодовая база — два окружения, без копипасты compose-файла.

## Задача

Для стека из lab2 (или pro03) сделайте:

1. `docker-compose.yml` — общая база (то, что одинаково везде).
2. `docker-compose.override.yml` — dev-окружение: код приложения
   смонтирован томом внутрь контейнера (правки видны без пересборки),
   включён debug, порт приложения наружу.
3. `docker-compose.prod.yml` — prod: образ тянется из реестра
   (не build), `restart: always`, лимиты ресурсов из pro06, секреты
   только через env-файл, который НЕ коммитится.
4. Команды запуска: dev — просто `docker compose up`; prod —
   `docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d`.

## Критерий приёмки

Обе конфигурации поднимаются; в dev правка `app.py` видна без пересборки,
в prod — `docker compose config` показывает итоговый объединённый файл.
Ответ: как именно compose объединяет несколько файлов (что перекрывает
что)?
