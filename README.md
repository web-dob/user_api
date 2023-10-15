# API Сервис авторизации

Перед запуском команды сборки сервиса, в корне необходимо разместить файл .env следующего содержания:
```
SECRET_KEY=Ваш SECRET_KEY
DEBUG=False
POSTGRES_HOST='dobapp_postgres'
POSTGRES_PORT=5432
POSTGRES_PASSWORD=Ваш пароль user для БД сервиса
POSTGRES_USER=Ваш user для БД сервиса
POSTGRES_DB=Название БД
STATIC_ROOT='static'
MEDIA_ROOT='media'
NGINX_EXTERNAL_PORT=Порт доступа к сервису
```

Команда сборки сервиса:
```
docker compose build
docker compose up -d
```

URL для проверки готовности сервиса:
```
http://0.0.0.0:<NGINX_EXTERNAL_PORT>/auth/register
```

Зависимости сервиса:
```
PostgreSQL
```