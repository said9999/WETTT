# CS5224 Project WETTT

## Project Structure

- api
  - contract between backend and frontend
- app
  - backend logic and api
- web
  - frontend (dist)
- lib
  - Python library
- ui-src
  - frontend (src)

## Install Dependency
`pip install -r requirements.txt`
`export PYTHONPATH=$(pwd):$PYTHONPATH` Add project root folder to pythonpath

## Make command (non-windows)
- `make dev`: start server in dev mode
- `make start`: start server in production mode
- `make image`: build app docker image
- `make docker_run`: start server within docker env

## For windows
- `flask run --port=8080`

## Making changes to UI and publishing to main app
- [First time] run `npm install` in 'ui-src' folder
- `ng serve` to build and serve app
- Access from localhost:4200
- Make changes if ncessary
- `ng build --prod` to prepare files for dist
- Copy files from 'dist' subfolder to 'web'