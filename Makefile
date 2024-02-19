install:
	poetry install

dev:
	poetry run uvicorn shortener_app.main:app --reload

lint:
	poetry run flake8
