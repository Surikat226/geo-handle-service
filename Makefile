# Установка (синхронизация) зависимостей через пакетный менеджер uv и запуск сервиса
run:
	uv sync
	uv run uvicorn app.main:app