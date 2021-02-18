# AgingHub
A web app for aiding the research community in understanding genes involved in aging

_v0.1.0_

## Dev Setup
- Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
- Clone this repo
- `cd AgingHub`
- `conda env create -f=environment.yml`
- `conda activate aginghub`

## Debugging
_Assumes you are using VS Code as your IDE_

#### Individual Python Module
- Run the `Python: Module` configuration from the debug panel
- Set breakpoints as desired

#### While Running Flask
- Run the `Python: Flask` configuration from the debug panel
- Set breakpoints as desired

## Running Tests
- Backend: `pytest`
- Frontend: `npm run test`

## Running the App via Gunicorn Outside of Docker
- `export HTTP_PORT=8000`
- `gunicorn -c gunicorn.conf.py "aginghub:create_app()"`

## Running the App via Docker
- Make sure it's stopped first: 
    - `docker stop aginghub`
    - `docker rm aginghub`
- `cd AgingHub`
- Update environment variables in the `Dockerfile` as needed
- `docker build -t aginghub .`
- `docker run -dp 80:80 --name aginghub aginghub`
- Go to `localhost` in your browser
- You should see a message now
- Viewing logs: `docker logs aginghub --follow`



