[![pipeline status](https://gitlab.crja72.ru/django_2023/students/145633-diiimali-47329/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django_2023/students/145633-diiimali-47329/pipelines)


Инструкция по запуску проекта на linux:

1. Склонировать репозиторий:
```bash
git clone git@gitlab.crja72.ru:django_2023/students/145633-diiimali-47329.git
```
2. Создать виртуальное окружение:
```bash
python3 -m venv venv
```
3. Активировать виртуальное окружение:
```bash
source venv/bin/activate
```
4. Создать файл .env:
```bash
touch .env
```
5. Обновить pip:
```bash
pip3 install --upgrade pip
```
6.1 Для работы в прод-режиме необходимо выполнить:
```bash
pip3 install -r requirements/prod.txt
```
Заполнить файл .env, как пример использовать .env-example. Вместо some_key подставить SECRET_KEY из settings.py, DJANGO_DEBUG=False, добавить необходимые хосты в DJANGO_ALLOWED_HOSTS.

6.2 Для работы в дев-режиме необходимо выполнить:
```bash
pip3 install -r requirements/dev.txt
```
Заполнить файл .env, как пример использовать .env-example. Вместо some_key подставить SECRET_KEY из 
settings.py, DJANGO_DEBUG=True.

6.3 Для работы в тест-режиме необходимо выполнить:
```bash
pip3 install -r requirements/test.txt
```
Заполнить файл .env, как пример использовать .env-example. Вместо some_key подставить SECRET_KEY из 
settings.py, DJANGO_DEBUG=True.

7. Запустить проект:
```bash
cd lyceum/
python3 manage.py runserver
```

Инструкция по запуску проекта на windows:

1. Склонировать репозиторий:
```
git clone git@gitlab.crja72.ru:django_2023/students/145633-diiimali-47329.git
```
2. Создать виртуальное окружение:
```
python -m venv venv
```
3. Активировать виртуальное окружение:
```
venv\Scripts\activate.bat
```
4. Создать файл .env:
```
notepad .env
```
5. Обновить pip:
```
pip install --upgrade pip
```
6.1 Для работы в прод-режиме необходимо выполнить:
```
pip install -r requirements/prod.txt
```
Заполнить файл .env, как пример использовать .env-example. Вместо some_key подставить SECRET_KEY из settings.py, DJANGO_DEBUG=False, добавить необходимые хосты в DJANGO_ALLOWED_HOSTS.

6.2 Для работы в дев-режиме необходимо выполнить:
```
pip install -r requirements/dev.txt
```
Заполнить файл .env, как пример использовать .env-example. Вместо some_key подставить SECRET_KEY из 
settings.py, DJANGO_DEBUG=True.

6.3 Для работы в тест-режиме необходимо выполнить:
```
pip install -r requirements/test.txt
```
Заполнить файл .env, как пример использовать .env-example. Вместо some_key подставить SECRET_KEY из 
settings.py, DJANGO_DEBUG=True.

7. Запустить проект:
```
cd lyceum/
python manage.py runserver
```
