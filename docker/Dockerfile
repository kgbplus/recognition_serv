FROM tiangolo/uvicorn-gunicorn:python3.11

ARG MODE

ENV MODE=${MODE}

COPY ./requirements/base.txt .
RUN pip install -r base.txt

COPY ./scripts /app
COPY ./recognition_serv /app
WORKDIR /app
