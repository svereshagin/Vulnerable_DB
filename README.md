Этот проект представляет собой демонстрацию уязвимостей веб-приложений к SQL-инъекциям. Он позволяет понять, как недостатки в защите базы данных могут привести к возможности взлома, и учит исправлять эти проблемы с использованием параметризованных запросов.

## Table of Contents
- [Project Structure](#project-structure)
- [Project Description](#project-description)
- [Installation and Setup](#installation-and-setup)
- [Usage Examples](#tests)
---

## Project Structure
```plaintext
├── README.md
├── __pycache__
│   ├── app.cpython-312.pyc
│   └── db.cpython-312.pyc
├── app.py
├── db.py
├── requirements.txt
├── static
│   ├── Octocat.png
│   └── main.css
├── templates
│   ├── error.html
│   ├── index.html
│   └── success.html
└── vulnerable.db
```
## Project Description

README - cодержит описание проекта
app.py — основной файл приложения Flask.
db.py — файл для работы с базой данных.
static - статичные файлы

Запускается с помощью команды python3 app.py.
Содержит маршруты /, /success, и /error.
На главной странице (/) располагается форма логина, в которую пользователь вводит имя пользователя и пароль. Проверка введённых данных осуществляется через вызов функции check_credentials из файла db.py.

db.py Включает две основные функции:
init_db() — создаёт таблицу users в базе данных vulnerable.db с двумя полями: username и password. Также добавляет тестового пользователя (admin / password123).
check_credentials(username, password) — проверяет введённые учётные данные и уязвима к SQL-инъекциям. Здесь содержится основной недостаток безопасности: пользовательские данные напрямую подставляются в SQL-запрос, что позволяет злоумышленнику вставить произвольный SQL-код.
vulnerable.db — SQLite-база данных, автоматически создаётся с таблицей users, если её нет.
Как провести тест уязвимости
Чтобы провести тест уязвимости, запустите приложение и выполните один из следующих методов:

## Installation and Setup
VIDEO - be later
manual:
  ![image](https://github.com/user-attachments/assets/a62d3b65-1dc1-4e24-8362-482a930766ad)
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
  



## Usage Examples

1. Через веб-форму
Запустите приложение: python3 app.py.
Перейдите по адресу http://127.0.0.1:5000/.
В поле "Username" введите: admin' OR 1=1 --.
В поле "Password" введите любое значение (оно будет проигнорировано из-за SQL-инъекции).
Нажмите кнопку "Login".
Если приложение уязвимо, вы будете перенаправлены на /success, даже если неправильные данные были введены.
![image](https://github.com/user-attachments/assets/be40eedd-f9e0-416d-8eac-6f138f6d86b9)

2. Через команду curl
Используйте команду curl для выполнения POST-запроса:

```sh
curl -X POST http://127.0.0.1:5000/ \
     -d "username=admin' OR 1=1 --" \
     -d "password="
```
Если приложение уязвимо, вы получите ответ, содержащий перенаправление на страницу /success.
