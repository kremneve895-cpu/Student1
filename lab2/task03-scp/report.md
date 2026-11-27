## Задание 3. Передача файла из контейнера (scp)

### Ход работы

1. Создал файл внутри контейнера, не заходя в интерактивную сессию
   (команду передал прямо в ssh):
    ssh -i ~/.ssh/docker_lab_key -p 2222 root@localhost \
      'echo "Hello from container" > /root/testfile.txt'

2. Забрал файл с контейнера на хост:
    scp -i ~/.ssh/docker_lab_key -P 2222 root@localhost:/root/testfile.txt ./
   Вывод:
    testfile.txt                                                                           100%   21    17.1KB/s   00:00
   Проверил содержимое на хосте:
    cat testfile.txt
    Hello from container

3. Создал файл на хосте и отправил его в контейнер:
    echo "Hello from host" > hostfile.txt
    scp -i ~/.ssh/docker_lab_key -P 2222 hostfile.txt root@localhost:/root/
   Вывод:
    hostfile.txt                                                                           100%   16    24.4KB/s   00:00

4. Прочитал файл внутри контейнера с хоста:
    ssh -i ~/.ssh/docker_lab_key -p 2222 root@localhost 'cat /root/hostfile.txt'
   Вывод:
    Hello from host

### Доказательство для отчёта

Вывод cat testfile.txt на хосте:
    Hello from container

Вывод cat /root/hostfile.txt в контейнере (прочитан через ssh):
    Hello from host

### Вывод

Настроена двусторонняя передача файлов между хостом и контейнером
через scp поверх SSH, с аутентификацией по ключу и без пароля.
Важный нюанс: у scp порт задаётся опцией -P (большая буква),
а у ssh — -p (маленькая). Команду можно передавать ssh'у напрямую
без интерактивного входа: ssh ... 'command' — это удобно для
одиночных операций.
