Финальная версия API, в которой применены все знания теоретической части по 
теме
django-rest-framework. Это социальная сеть для публикации своих постов. 
Поддерживает разные тематические группы. Авторство и подписки.  
___
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?
style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?
style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?
style=for-the-badge&logo=sqlite&logoColor=white)

![GitHub code size in bytes](https://img.shields.
io/github/languages/code-size/26remph/api_final_yatube)
![GitHub repo size](https://img.shields.
io/github/repo-size/26remph/api_final_yatube)
![GitHub](https://img.shields.io/github/license/26remph/api_final_yatube)
![pythonversion](https://img.shields.io/badge/python-%3E%3D3.7-blue)

## Оглавление
1. [Как запустить проект](#как-запустить-проект)
2. [Создание пользователей](#cоздание-пользователей)
3. [Документация по api для yatube](#документация-по-api)
4. [Поиск в базе данных](#поиск-в-базе-данных)
5. [Демонстрационная версия API](#Демонстрационная-версия-API)
6. [Об авторе](#об-авторе)
7. [Контрольная сумма репозитария](#контрольная-сумма-проекта)

### Как запустить проект  
- клонировать репозиторий и перейти в него в командной строке:  
```
git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram
```  


- создать и активировать виртуальное окружение:  
```md
python -m venv venv
venv/Scripts/activate
```
- установить зависимости из файла requirements.txt:  
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- выполнить миграции:
```
python manage.py migrate
```  
- запустить проект:
```
python manage.py runserver
```

### Создание пользователей
Создание пользователей через API не предусмотрено. Работа с API доступна, 
- только авторизированным пользователям через JSON WEB Token (JWT). Как 
  получить и установить токен [читайте ниже](#авторизация-API-пользователей). 

Для создания пользователей имеющих доступ к API вам необходимо созадать 
суперпоьзователя и войти под ним в админ панель.
Для создания суперпользователя вызовите следующую команду из той же папки, 
где расположен **manage.py**. Вас попросят ввести имя пользователя, адрес 
электронной почты и надёжный пароль. 
```md
python3 manage.py createsuperuser 
```
Для входа в админ-панель откройте ссылку /admin (например http://127.0.0.
1:8000/admin) и введите логин и пароль вашего нового суперпользователя (вас 
перенаправят на login-страницу и потом обратно на /admin после ввода всех 
деталей).  
[[подробнее]](https://developer.mozilla.
org/ru/docs/Learn/Server-side/Django/Admin_site)

###Авторизация API пользователей. 
После регистрации пользователей вам и каждомму из зарегистрированных 
пользователей будут дступны два эндпоинта для создания токенов авторизации.

| Эндпоинт                                      | Описание                  |
|-----------------------------------------------|---------------------------|
| http://127.0.0.1:8000/api/v1/jwt/create/      | Получение JWT-токена      |
| http://127.0.0.1:8000/api/v1/jwt/refresh/     | Обновление JWT-токена.    |
| http://127.0.0.1:8000/api/v1/jwt/verify/      | Проверка JWT-токена       |

Для получения токена отправьте POST запрос с данными в формате JSON 
следующего вида. 
```json
{
  "username": "string",
  "password": "string"
}
```
В ответ придет json ответ:
```json
{
    "refresh": "string",
    "access": "string"
}
```
Для доступа к апи используйте токен из поля `access`, тип авторизации при 
запросах: Bearer Token.
Данные эндпоинты доступны без авторизации, остальные энпоинты доступны в 
большинстве своем, только авторизированным пользователям. Полный перечень 
эндпоинтов, их подробное описание представлено в [документации к API]
(#документация-по-API)

### Документация по API

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет 
доступна документация для **API Yatube**.  
Документация представлена в формате [Redoc](https://github.com/Redocly/redoc).

### Поиск в базе данных
По умолчанию к проекту подключена база данны sqlite
и встроенный бэкенд `SearchFilter`. Встроенные фильтрующие бэкенды 
импортируются из библиотеки `filters`.   
[[подробнее]](https://www.django-rest-framework.
org/api-guide/filtering/#searchfilter) 

Это накладывает определенные ограничения.
- поиск можно вести только по текстовым полям
- при использовании базы данных sqlite поиск нечувствителен к регистру 
  только при запросах на латинице  

Можно искать по нескольким совпадениям: в запросе их надо разделить 
запятыми, без пробелов.
Например, при запросе http://127.0.0.1:8000/posts/?search=Сн,ок в выдачу 
попадут только те посты, где в тексе есть одновременно все совпадения, 
например — «Снежок».

Поиск можно производить с использованием [регулярных выражений]
(https://regex101.com/), что существенно облегчает задачу и повышает 
гибкость текстового поиска.


### Об авторе
Konstantin Saraev,  
студент 49 когорты,  
Яндекс Практикум  
:e-mail: badmantegrow1@gmail.com


<p>
    <span>© 2023, Konstantin, Inc., temet nosce ツ </span>
</p>
