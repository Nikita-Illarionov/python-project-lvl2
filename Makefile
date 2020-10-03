install:
	poetry install

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest tests --cov=gendiff

