# CS5224 Project WETTT

## Project Structure

- app
  - backend API
- web
  - frontend
- lib
  - Python library

## Install Dependency
`pip install -r requirements.txt`
`export PYTHONPATH=$(pwd):$PYTHONPATH` Add project root folder to pythonpath

## Make command
- `make dev`: start server in dev mode
- `make start`: start server in production mode
- `make image`: build app docker image
- `make docker_run`: start server within docker env
