PORT ?= 3001

dev:
	poetry run uvicorn main:app \
		--port $(PORT) \
		--app-dir ./src \
		--reload

test\:unit:
	poetry run pytest -v

test\:static:
	make -j 2 check\:lint check\:format

check\:lint:
	poetry run pyright src

check\:format:
	poetry run black src