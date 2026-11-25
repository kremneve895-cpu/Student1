## Задание 1. SSH-сервер в контейнере

### Ход работы

1. Запустил контейнер с пробросом порта:
    docker run -d -p 2222:22 --name ubuntu-ssh ubuntu sleep infinity
   (контейнер с таким именем уже существовал с прошлого запуска — удалил его
   командой docker rm -f ubuntu-ssh и создал заново)

2. Установил SSH-сервер внутри контейнера:
    docker exec -it ubuntu-ssh bash
    apt-get update
    apt-get install -y openssh-server
    mkdir -p /run/sshd

3. Разрешил вход по ключу через sed:
    sed -i 's/^#\?PubkeyAuthentication.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config
    sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin prohibit-password/' /etc/ssh/sshd_config

4. Запустил sshd: /usr/sbin/sshd, вышел из контейнера (exit)

5. Проверил с хоста:
    ssh -p 2222 root@localhost

### Баннер SSH из шага 5

The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is: SHA256:CWnr+MsonV/u7iBQSFwluLVTVGQdClN/8AKg7tzmCcE
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2222' (ED25519) to the list of known hosts.
root@localhost's password:

Сервер ответил отпечатком своего ключа и дошёл до запроса пароля —
значит, SSH-сервер внутри контейнера работает и принимает подключения.
Пароль не задавался, попытку входа прервали (Ctrl+C).

Примечание: при первом подключении ssh выдал предупреждение
"REMOTE HOST IDENTIFICATION HAS CHANGED!" — это произошло потому,
что контейнер был пересоздан, и sshd сгенерировал новые ключи,
а в known_hosts на хосте остался отпечаток старого контейнера.
Старую запись удалили командой:
    ssh-keygen -f '/home/evgenius/.ssh/known_hosts' -R '[localhost]:2222'

### Вывод

Контейнер Ubuntu превратился в работающий SSH-сервер: он слушает
порт 22 внутри, а на хосте доступен через порт 2222. При подключении
ssh видит отпечаток ключа сервера и запрашивает аутентификацию.
Вход по паролю отключён (PermitRootLogin prohibit-password) — в
задании 2 настроим вход по SSH-ключу.
