install:
	poetry install

dev:
	poetry run uvicorn shortener_app.main:app --reload

lint:
	poetry run flake8

start:
	poetry run uvicorn shortener_app.main:app --host 0.0.0.0 --port 10000
