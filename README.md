# Picture feed 
__________________
## Мини-приложение, которое позволяет размещать файлы различного формата (jpg, png, svg, mp4, zip, doc, pdf), а также оставлять под ними комментарии. ##
____
## Stack:
 - Python3.10
 - FastAPI
 - Postgres
____
## Запуск проекта
1. Создать виртуальное окружение;
2. Установить зависимости из requirements.txt:
- pip install -r requirements.txt
3. Создать контейнер для PostgreSQL:
- docker run --name "название проекта" -e POSTGRES_PASSWORD="придумать" -p порт:порт -d postgres
4. Накатить миграции:
- alembic revision --autogenerate -m "Commit"
- alembic upgrade head
5. Запустить сервер:
- cd src
- unicorn main:app --reload
___

### Документауия к API:
1. По ссылке:
- #### https://app.swaggerhub.com/apis/MKARPENKO96/fast-api/0.3.0
2. После запуска сервера локально:
- #### https://127.0.0.1:8000/docs
