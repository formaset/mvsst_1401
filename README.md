# АНО «МосводостокСтройТрест» — сайт на Django + Wagtail

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py bootstrap_site
python manage.py runserver
```

Откройте сайт на `http://127.0.0.1:8000/`.

## Статика и медиа

Сборка статики:

```bash
python manage.py collectstatic
```

Медиа-файлы хранятся в `MEDIA_ROOT` (по умолчанию `./media`). Для загрузки медиа достаточно загрузить файлы через админку или скопировать их в папку.

## Перенос админки

Путь админки меняется через переменную окружения `ADMIN_PATH`.

Пример для `.env`:

```
ADMIN_PATH=control
```

## Переключение БД на MySQL

По умолчанию используется SQLite. Для MySQL установите драйвер `mysqlclient` и задайте параметры в `.env`:

```
DB_ENGINE=django.db.backends.mysql
DB_NAME=mvsst
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

## Инициализация контента

Команда `bootstrap_site` создаёт стартовые страницы и демо-контент:

```bash
python manage.py bootstrap_site
```

## Переменные окружения

Смотрите `.env.example`.
