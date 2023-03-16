# Foodgram ![Foodgram Status](https://github.com/vadikray/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)
## Документация проекта: http://130.193.42.203/api/docs/

## Описание

Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.

## инструкция
Клонируйте репозиторий
```
git@github.com:Vadikray/foodgram-project-react.git
```
Перейдите в infra
```
cd infra
```
Запуск docker-compose
```
docker-compose up -d --build
```
Выполните по очереди команды(Применение миграций, создания суперпользователя и собрать статику)
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```
Команда для заполнения базы данными 
```
docker-compose exec web python manage.py loaddata fixtures.json
```
Команда для заполнения базы ингредиентов
```
docker-compose exec backend python manage.py load_ingredients
```


Шаблон наполнения .env
```

DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DJANGO_KEY=&25k@3hm-s1d)5c-zu3_45ycih+!5&717(b$*d)zg341xo#p$e
```

Данные для проверки работы приложения: Суперпользователь:
```
username admin
email: admin@gmail.com
password: admin
```

# Автор:
---Конюшков В.А.---