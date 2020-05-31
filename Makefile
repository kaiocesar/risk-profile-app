SHELL := /bin/bash

up: 
	docker-compose up --build

dw:
	docker-compose down

test:
	docker-compose run app sh -c "python manage.py test"

lint:
	docker-compose run app sh -c "flake8"
