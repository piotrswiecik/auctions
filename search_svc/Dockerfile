FROM python:3.12-slim as BUILD

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app"]

FROM python:3.12-slim

WORKDIR /app

COPY --from=BUILD /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

COPY src/ .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "search.main:app", "--host", "0.0.0.0"]