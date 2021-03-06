# AgingHub
A web app for aiding the research community in understanding genes involved in aging

_v0.1.0_


## Dev Setup
- Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
- Clone this repo
- `cd AgingHub`
- `conda env create -f=environment.yml`
- `conda activate aginghub`

## Running the App
- Make sure it's stopped first: `docker stop aginghub; docker rm aginghub`
- `cd AgingHub`
- Update environment variables in the `Dockerfile` as needed
- `docker build -t aginghub .`
- `docker run -dp 80:80 --name aginghub aginghub`
- Go to `localhost` in your browser
- You should see a message now
- Viewing logs: `docker logs aginghub --follow`

## Testing
- Run `pytest`

## Test Coverage
- Run `coverage run -m pytest` to generate the report
- Next, `coverage report -m` to view the results

