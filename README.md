### Документация


# Пакеты для установки
/backend
pip install -r requirements.txt

/frontend
npm install node-sass
npm install axios
npm install react-router-dom

# Миграции
alembic init -t async migrations  -  инициализация ассинхронного алембика(при деплое приложения)
alembic revision --autogenerate -m "comment"  -  создание миграции
alembic upgrade heads  -  усвоение миграции