<div align=center>
  
  # [Foodgram](https://foodgram.servehttp.com/) продуктовый помощник
  
  [![Foodgram_CI/CD](https://github.com/JustLight1/foodgram-project-react/workflows/Foodgram_CI/CD/badge.svg)](https://github.com/JustLight1/kittygram_final/workflows/CICD-Kittygram/badge.svg)
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  
  ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)


</div>

## Описание проекта


Foodgram - онлайн-сервис, представляющий собой продуктового помощника как для начинающих кулинаров, так и для опытных гурманов. В рамках этого сервиса пользователи могут делиться своими рецептами, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список избранного, а также скачивать сводный список продуктов в формате .pdf перед походом в магазин для приготовления выбранных блюд.


## Подготовка сервера и деплой проекта

1. Создать директорию foodgram/ в домашней директории сервера.

2. В корне папки foodgram поместить файл .env, заполнить его по шаблону

  ```env
    ALLOWED_HOSTS=<Ваш домен>, <IP сервера>
    DEBUG=False

    POSTGRES_USER=...
    POSTGRES_PASSWORD=...
    POSTGRES_DB=...
    
    DB_HOST=...
    DB_PORT=...
```

4. Установить Nginx и настроить конфигурацию так, чтобы все запросы шли в контейнеры на порт 9090.

    ```bash
        sudo apt install nginx -y 
        sudo nano etc/nginx/sites-enabled/default
    ```
    
    Пример конфигурация nginx
    ```bash
        server {
            server_name <Ваш IP> <Домен вашего сайта>;
            server_tokens off;
            client_max_body_size 20M;
        
            location / {
                proxy_set_header Host $http_host;
                proxy_pass http://127.0.0.1:9000;
        }
    ```
    
    > При необходимости настройте SSL-соединение

5. Установить docker и docker-compose
   
``` bash
    sudo apt update
    sudo apt install curl
    curl -fSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh
    sudo apt-get install docker-compose-plugin     
```

4. Добавить в Secrets GitHub Actions данного репозитория на GitHub переменные окружения

``` env
    DOCKER_USERNAME=<имя пользователя DockerHub>
    DOCKER_PASSWORD=<пароль от DockerHub>
    
    USER=<username для подключения к удаленному серверу>
    HOST=<ip сервера>
    PASSPHRASE=<пароль для сервера, если он установлен>
    SSH_KEY=<ваш приватный SSH-ключ>
    
    TELEGRAM_TO=<id вашего Телеграм-аккаунта>
    TELEGRAM_TOKEN=<токен вашего бота>
```
5. Запустить workflow проекта выполнив команды:

```bash
  git add .
  git commit -m ''
  git push
```

## Сервис разрабатывали:
<details>
<summary>
<h4>Backend:</h4>
</summary>

<br>

**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)

**Ванданова Мария**

[![Telegram Badge](https://img.shields.io/badge/-vandanova_maria-blue?style=social&logo=telegram&link=https://t.me/vandanova_maria)](https://t.me/vandanova_maria) [![Gmail Badge](https://img.shields.io/badge/handarkin@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:handarkin@gmail.com)](mailto:handarkin@gmail.com)

**Калинина Юлия**

[![Telegram Badge](https://img.shields.io/badge/-good_old_user-blue?style=social&logo=telegram&link=https://t.me/good_old_user)](https://t.me/good_old_user) [![Gmail Badge](https://img.shields.io/badge/deamanda@ya.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:deamanda@ya.ru)](mailto:deamanda@ya.ru)


**Тутункин Владислав** 

[![Telegram Badge](https://img.shields.io/badge/-tvladislav94-blue?style=social&logo=telegram&link=https://t.me/tvladislav94)](https://t.me/tvladislav94) [![Gmail Badge](https://img.shields.io/badge/vladislav-login94@yandex.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:vladislav-login94@yandex.ru)](mailto:vladislav-login94@yandex.ru)

</details>