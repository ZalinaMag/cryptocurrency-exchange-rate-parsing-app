Проект для мониторинга цен на криптовалюты и отправки уведомлений через email.

## Требования

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Как развернуть проект

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ZalinaMag/my-crypto-app.git
   cd my-crypto-app

   ```

2. Запустите проект с помощью Docker Compose:
   docker-compose up --build

   Это команда:
   Соберет образ для вашего приложения.
   Запустит PostgreSQL, MailCatcher и CloudBeaver.

3. Откройте MailCatcher для просмотра отправленных писем.

4. Откройте CloudBeaver для управления базой данных PostgreSQL.

5. Чтобы остановить контейнеры выполните команду:
   docker-compose down

Управление базой данных через CloudBeaver
Откройте CloudBeaver и зарегистрируйтесь в качестве администратора
Настройте подключение к PostgreSQL:
Host: IP адрес контейнера с Postgres внутри Докера, посмотреть IP можно командой docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres
Port: 5432
User: postgres
Password: your_password

6. Скрипт my_crypto_container будет регулярно ходить по ресурсам из задания и выполнять запросы к базе данных и почтовому серверу согласно алгоритму.
