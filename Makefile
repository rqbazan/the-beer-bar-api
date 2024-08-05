PORT ?= 3001

dev:
	uvicorn main:app \
		--port $(PORT) \
		--app-dir ./src \
		--reload

test:
	pytest