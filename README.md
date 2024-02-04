![example workflow](https://github.com/Michelin90/api_yamdb/actions/workflows/main.yml/badge.svg?style=for-the-badge)
# api_yamdb

## Авторы:
Михаил [Michelin90](https://github.com/Michelin90) Хохлов

Дарья [Daria0008](https://github.com/Daria0008) Солдатова

Евгений [Jossepik](https://github.com/Jossepik) Будницкий 

## Описание:
Проект YaMDb собирает отзывы пользователей на произведения. 
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть 
фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», 
«Музыка». Например, в категории «Книги» могут быть произведения 
«Винни-Пух и все-все-все» и «Марсианские хроники», а в категории 
«Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха.

## Язык и инструменты:
[![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-blue?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![REST_FRAMEWORK](https://img.shields.io/badge/Django_REST_framework-3.12-blue?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Michelin90/api_yamdb
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать в корневой папке проекта файл **.env** и добавить в него следующие строки:
```
SECRET_KEY=<ваш секретный ключ для django-приложения>
EMAIL_HOST_USER=<адрес электронной почты, с которой будет осуществляться отправка кода подтверждения>
EMAIL_HOST_PASSWORD=<пароль от почтового ящика, либо специальный пароль для внешнего приложения>
EMAIL_HOST=<адрес сервера исходящей почты (SMTP-сервер)>
EMAIL_PORT=<порт>
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Проект будет доступен по адресу: http://127.0.0.1:8000/

### Подробная документация  проекта в формате ReDoc доступна по адресу:
http://127.0.0.1:8000/redoc/