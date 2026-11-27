## Задание 2. Вход по ключу без пароля

### Ход работы

1. Сгенерировал SSH-ключ на хосте:
    ssh-keygen -t ed25519 -f ~/.ssh/docker_lab_key -N ""
   Получил пару файлов:
   - ~/.ssh/docker_lab_key — приватный ключ
   - ~/.ssh/docker_lab_key.pub — публичный ключ

2. Посмотрел публичный ключ:
    cat ~/.ssh/docker_lab_key.pub
   Вывод:
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG99zNwIpbXXGypo9cZgjUbItKUKnqYqHamU3vNzt3Qh evgenius@DESKTOP-JNKRNML

3. Добавил публичный ключ в контейнер:
    docker exec -it ubuntu-ssh bash
   Внутри:
    mkdir -p /root/.ssh
    chmod 700 /root/.ssh
    echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG99zNwIpbXXGypo9cZgjUbItKUKnqYqHamU3vNzt3Qh evgenius@DESKTOP-JNKRNML" >> /root/.ssh/authorized_keys
    chmod 600 /root/.ssh/authorized_keys
    exit
   (В первый раз запись не сохранилась — сессия закрылась до выполнения echo,
   повторил команды, проверил cat'ом, что authorized_keys на месте.)

4. Вошёл по ключу без пароля:
    ssh -i ~/.ssh/docker_lab_key -p 2222 root@localhost
   Пароль не запрашивался — вход выполнен по ключу. Внутри сразу вышел (exit).

### Доказательство входа без пароля

Вывод команды:
    ssh -i ~/.ssh/docker_lab_key -p 2222 root@localhost hostname

Результат:
    53c79b41ad12

Команда выполнена с хоста, пароль не запрашивался, и она отработала внутри
контейнера: 53c79b41ad12 — это hostname (id) контейнера ubuntu-ssh.
Значит, аутентификация прошла по публичному ключу из /root/.ssh/authorized_keys.

### Вывод

Настроен вход в контейнер по SSH-ключу: приватный ключ лежит на хосте,
публичный — в /root/.ssh/authorized_keys контейнера с правами 600
(папка /root/.ssh — 700). В задании 1 вход по паролю был отключён
(PermitRootLogin prohibit-password), поэтому доступ возможен только по ключу —
это в точности модель боевого сервера: пароли отключены, доступ по ключу.
