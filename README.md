# :poop: Интернет-маркетплейс на Django
> Pet-проект. Создается в целях более лучшего изучения Django :shipit:

## :memo: [Changelog](https://github.com/Re-Gelu/Sample_shop/blob/master/changelog.txt)

## :triangular_ruler: Стек проекта: 
- Python (Django, Django REST)
- HTML5
- CSS (Bootstrap 5, UIkit)
- NGNIX, Gunicorn
- Celery, Redis

## :package: Зависимости проекта
```
Django==4.0.8
djangorestframework==3.13.1
django-filter==22.1
FileBrowser==1.1.3
django-filebrowser-no-grappelli==4.0.1
django-tinymce==3.5.0
django-admin-interface==0.20.0
django-extra-settings==0.6.1
django-phonenumber-field[phonenumbers]==7.0.0
django_crispy_forms==1.14.0
crispy-bootstrap5
celery[redis]==5.2.7
django-celery-results==2.4.0
django-celery-beat==2.3.0
django-allauth
django-debug-toolbar
redis==4.3.4
pyQiwiP2P==2.0.6
shortuuid==1.0.9
Markdown==3.4.1
psycopg2-binary==2.9.3
Pillow==9.2.0
gunicorn==20.1.0
art==5.7
pytz==2022.4
tzdata==2022.5
```

## :closed_lock_with_key: Настройка входа в админку

- `$ python manage.py createsuperuser --username admin --email admin@email.com`
- `$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser --username admin@email.com --email admin@email.com`

## :black_nib: Авто-заполнение магазина для быстрого тестирования

```
.../db_auto_fill/7/Categories/
```
```
.../db_auto_fill/10/Subcategories/
```
```
.../db_auto_fill/300/Products/
```

> Необходимы права администратора

## :moneybag: Оплата

Реализована при помощи QIWI, проверка оплаты происходит при помощи задач Celery по расписанию.

Требуется обязательно установить приватный ключ QIWI в админке или settings.py / .env файлах.
Получить можно тут: https://qiwi.com/p2p-admin/api

- Команды Celery 

  ```
    Windows:
  $ celery -A Site beat --loglevel=info
  $ celery -A Site worker --loglevel=info /  $ celery -A Site worker --pool=solo --loglevel=info
  
    Linux:
  $ celery -A Site worker --beat --loglevel=info
  ```

## :whale: Работа с Docker

- Удаление контейнеров

  ```
  $ docker-compose down -v
  ```

- Поднять Dev контейнер
  ```
  $ docker-compose -f docker-compose.yml up -d --build
  ```

- Поднять Prod контейнер
  ```
  $ docker-compose -f docker-compose.prod.yml up -d --build
  $ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
  $ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
  ```
  
## :camera: Скрины проекта
![Изображение №1](https://user-images.githubusercontent.com/75813517/199733106-cda4086c-11d1-431b-a853-0b00bdeb165f.png)
![Изображение №2](https://user-images.githubusercontent.com/75813517/199733450-389a54c8-18d5-4f43-b9c8-ddaeab7486c9.png)
![Изображение №3](https://user-images.githubusercontent.com/75813517/199733692-bf94269c-043a-45d9-818a-8430408c75e7.png)
![Изображение №4](https://user-images.githubusercontent.com/75813517/199733891-7cf053ef-2f34-43bb-bb8e-d247c6f5ba80.png)
![Изображение №5](https://user-images.githubusercontent.com/75813517/199734053-debf4bfa-14cd-4771-9414-af2f56fe2bc6.png)
![Изображение №6](https://user-images.githubusercontent.com/75813517/199734154-a2008491-838e-4af6-96a8-0775d38821c8.png)
![Изображение №7](https://user-images.githubusercontent.com/75813517/199734251-e7d27528-c5ac-4bb0-9a61-b8c290af1232.png)
![Изображение №8](https://user-images.githubusercontent.com/75813517/199734371-bec5cfc7-9a35-4011-8af7-5e70a798f8c2.png)
![Изображение №9](https://user-images.githubusercontent.com/75813517/199734488-5ae111bf-a545-4282-bed3-4ca41206a0ec.png)



