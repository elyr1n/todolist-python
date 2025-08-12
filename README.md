# ToDo List - Список задач (Шаблон на Django/Python)

Локальный запуск:

1. Установите зависимости:
```bash
python -m pip install -r requirements.txt
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Настройте переменные окружения:
```
SECRET_KEY='example'
```

4. Запустите миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```