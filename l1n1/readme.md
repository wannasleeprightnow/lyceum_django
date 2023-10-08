Инструкция по запуску проекта на linux:

1. Склонировать репозиторий:
```bash
git clone git@gitlab.crja72.ru:django_2023/students/145633-diiimali-47229.git
```
2. Создать виртуальное окружение:
```bash
python3 -m venv venv
```
3. Активировать виртуальное окружение:
```bash
source venv/bin/activate
```
4. Обновить pip и установить зависимости:
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
```
5. Запустить проект:
```bash
cd lyceum/
python3 manage.py runserver
```

Инструкция по запуску проекта на windows:

1. Склонировать репозиторий:
```
git clone git@gitlab.crja72.ru:django_2023/students/145633-diiimali-47229.git
```
2. Создать виртуальное окружение:
```
python -m venv venv
```
3. Активировать виртуальное окружение:
```
venv\Scripts\activate.bat
```
4. Обновить pip и установить зависимости:
```
pip install --upgrade pip
pip install -r requirements.txt
```
5. Запустить проект:
```
cd lyceum/
python manage.py runserver
```
