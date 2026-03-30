FROM python:3.12-slim

# Установка системных зависимостей для сборки
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Установка poetry
RUN pip install poetry

# Копируем конфиги зависимостей
COPY pyproject.toml poetry.lock* ./

# Отключаем создание виртуального окружения (в контейнере оно не нужно)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем проект
COPY . .

# Делаем скрипт запуска исполняемым (создадим его на следующем шаге)
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]