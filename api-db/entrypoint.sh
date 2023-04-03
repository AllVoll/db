#!/bin/bash

# Выполнение миграций Alembic перед запуском приложения
alembic revision --autogenerate -m "Add primary key to ApiKey"
alembic upgrade head

# Запуск приложения
exec "$@"
