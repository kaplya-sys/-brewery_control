# Контроль процесса варки пива
## Описание:
На сайте возможность добавления цистерн для пива, вид дрожжей. Внесение измерений для таких критериев, как давление, температура, плотность и отображение их в графическом виде. А также есть возможность регистрации сотрудников, назначения задач с возможностью редактирования,  выполнения и удаления.
***
## Скриншоты:
<img src="https://i.postimg.cc/50YfwzFk/schedule.png" width="500" alt="Графики">
<img src="https://i.postimg.cc/dt8tHGNb/add-raw-material.png" width="500" alt="Склад">
<img src="https://i.postimg.cc/XvDVGLXC/register.png" width="500" alt="Регистрация сотрудника">
<img src="https://i.postimg.cc/RZdC94BG/add-task.png" width="500" alt="Добавление задачи">
<img src="https://i.postimg.cc/255kSMjY/task.png" width="500" alt="Задачи">

***
## Запуск с использованием _Docker_:
__Клонируйте репозиторий:__

    git clone https://github.com/alekseevwork/-brewery_control.git
    
__Создайте _.env_ файл и добавьте секретный ключ и адрес базы данных:__

    SECRET_KEY = 'надежный ключ'
    DATABASE_URI = 'база данных://логин:пароль@plocalhost:порт/имя базы данных'
    
__Создайте _.env.docker_ файл и добавьте логин, пароль и имя базы данных:__

    POSTGRES_DB = 'имя базы данных'
    POSTGRES_USER = 'логин'
    POSTGRES_PASSWORD = 'пароль'
    
__Выполните команду:__

    docker-compose up
    
__Добавить суперпользователя запустив _create_superuser.py_:__

    python3 create_superuser.py
    
***
## Запуск с без использования _Docker_:
__Клонируйте репозиторий:__

    git clone https://github.com/alekseevwork/-brewery_control.git
    
__Создайте виртуальное окружение и запустите:__
Windows:
    
    python -m venv env
    source env/bin/activate
    
Linux и Mac:

    python3 -m venv env
    env\Scripts\activate
    
__Создайте _.env_ файл и добавьте секретный ключ и адрес базы данных:__

    SECRET_KEY = 'надежный ключ'
    DATABASE_URI = 'база данных://логин:пароль@localhost:порт/имя базы данных'
    
__Установите необходимые пакеты:__
Windows:
    
    pip install -r requirements.txt
    
Linux и Mac:

    pip3 install -r requirements.txt
    
__Запустите проект:__
Windows:
    
    run.bat
    
Linux и Mac:

    chmod +x run.sh
    ./run.sh

__Добавить суперпользователя запустив _create_superuser.py_:__
Windows:
    
    python create_superuser.py
    
Linux и Mac:

    python3 create_superuser.py
