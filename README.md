# Доктор+

## Установка и запуск

1. Клонируйте репозиторий:
    ```
    git clone <URL>
    ```
2. Создайте виртуальное окружение:
    ```
    python -m venv env
    ```
3. Установите необходимые зависимости:
    ```
    pip install -r requirements.txt
    ```
4. Примените миграции и запустите сервер:
    ```
    python manage.py migrate
    python manage.py runserver
    ```
