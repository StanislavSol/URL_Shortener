install:
	poetry install

dev:
	poetry run uvicorn shortener.app:app --reload

lint:
	poetry run flake8
