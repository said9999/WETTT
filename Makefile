export PYTHONPATH := ./lib:$PYTHONPATH

IMAGE_NAME := cs5224proj:1.0
PORT ?= 8080
PWD := $(shell pwd)

dev:
	flask run --port=$(PORT)

start:
	gunicorn -b :$(PORT) app:app

image:
	docker image build -t $(IMAGE_NAME) . 

docker_run: image
	docker run $(IMAGE_NAME)
