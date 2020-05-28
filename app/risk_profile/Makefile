SHELL := /bin/bash

up:
	docker-compose up --build

dw:
	docker-compose down -v

mig:
	docker-compose exec app python manage.py migrate --noinput

test:
	docker-compose run app sh -c "python manage.py test && flake8"

