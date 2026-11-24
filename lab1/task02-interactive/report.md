## Задание 2. Интерактивный контейнер

### Ход работы

1. Запустил контейнер:

    docker run -it ubuntu bash

2. Внутри контейнера выполнил команды:

    root@00a4fbbee32c:/# ls
    bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

    root@00a4fbbee32c:/# whoami
    root

    root@00a4fbbee32c:/# cat /etc/os-release | head -2
    PRETTY_NAME="Ubuntu 26.04.1 LTS"
    NAME="Ubuntu"

3. На хостовой машине (WSL) выполнил ту же команду:

    evgenius@DESKTOP-JNKRNML:~$ cat /etc/os-release | head -2
    PRETTY_NAME="Ubuntu 26.04.1 LTS"
    NAME="Ubuntu"

    Вывод совпал: образ ubuntu:latest внутри контейнера оказался той же версии,
    что и WSL-хост. Изоляция при этом сохраняется — у контейнера своя файловая
    система, свои процессы и свой root.

4. Выйдя из контейнера командой exit, проверил список контейнеров:

    $ docker ps -a
    CONTAINER ID   IMAGE    COMMAND   CREATED         STATUS                     NAMES
    00a4fbbee32c   ubuntu   "bash"    2 minutes ago   Exited (0) 27 seconds ago  practical_moser

### Ответ на вопрос задания

docker ps показывает только работающие контейнеры, а docker ps -a — все,
включая остановленные. После exit завершился основной процесс контейнера
(bash), а контейнер живёт ровно столько, сколько живёт его главный процесс,
поэтому он перешёл в статус Exited (0). Контейнер не удаляется автоматически:
файловая система и данные сохраняются, его можно перезапустить командой
docker start -ai 00a4fbbee32c.
