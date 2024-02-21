install:
	poetry install
	$(MAKE) .env

dev:
	poetry run uvicorn shortener_app.main:app --reload

lint:
	poetry run flake8

start:
	poetry run uvicorn shortener_app.main:app --host 0.0.0.0 --port 10000

test:
	poetry run pytest shortener_app/tests.py

.env:
	test ! -f .env && cp .env.example .env
