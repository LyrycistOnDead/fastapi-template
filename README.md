🚀 FastAPI Production-Ready Template
Современный, типизированный шаблон для разработки масштабируемых API на Python. Вдохновлен архитектурными паттернами Clean Architecture и лучшими практиками экосистемы FastAPI.

✨ Особенности (Stack)
FastAPI — высокопроизводительный веб-фреймворк.

SQLAlchemy 2.0 — современная ORM с полной поддержкой типов и асинхронности.

Alembic — надежное управление миграциями базы данных.

PostgreSQL — основная реляционная БД.

Pydantic v2 — молниеносная валидация данных и схем.

Docker & Docker Compose — полная контейнеризация для быстрой развертки.

Poetry — современный менеджер зависимостей.

🏗 Архитектура проекта
Проект разделен на логические слои для удобства тестирования и поддержки:

📂 app/api — Эндпоинты (Роуты) и зависимости запросов.

📂 app/core — Глобальные настройки и конфигурации.

📂 app/db — Инициализация БД и сессий.

📂 app/models — SQLAlchemy модели (описание таблиц).

📂 app/repositories — Слой доступа к данным (CRUD операции).

📂 app/schemas — Pydantic схемы (валидация входных/выходных данных).

📂 app/services — Бизнес-логика приложения.

🛠 Быстрый запуск
1. Предварительные требования
Убедитесь, что у вас установлены Docker и Docker Compose.

2. Клонирование и настройка
Bash
git clone https://github.com/vash-akk/fastapi-template.git
cd fastapi-template
Создайте файл .env на основе примера (или используйте стандартные значения из docker-compose.yml).

3. Запуск через Docker
Bash
docker-compose up --build
Эта команда соберет образ, установит зависимости, применит миграции БД и запустит сервер.

🔗 Полезные ссылки
API Documentation (Swagger): http://localhost:8000/docs

ReDoc (Alt Docs): http://localhost:8000/redoc

Health Check: http://localhost:8000/api/v1/test/db-check

📝 Основные команды для разработки
Создание новой миграции (после изменения моделей):

Bash
docker-compose exec backend alembic revision --autogenerate -m "Description"
Применение миграций вручную:

Bash
docker-compose exec backend alembic upgrade head
Остановка проекта:

Bash
docker-compose down