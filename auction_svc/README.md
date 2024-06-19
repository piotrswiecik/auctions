# Auction service

tbd

## Running in development

To run the service in isolation for debugging / hot reload

```shell
# from microservice root
cd <project_root>/auction_svc

# install dependencies
poetry install --no-root
# or
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

# install package in editable dev mode
python -m pip install --editable .
python -m uvicorn run auctions.main:app --reload --host 0.0.0.0
```
