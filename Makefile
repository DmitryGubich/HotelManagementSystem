venv 		:= source .venv/bin/activate
cd_app 		:= cd app
app_cmd 	:= docker-compose exec app

start:
	docker-compose up

start-app:
	docker-compose up app db

test:
	$(app_cmd) pytest

stop:
	docker-compose stop
