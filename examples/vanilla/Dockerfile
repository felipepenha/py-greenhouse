FROM python:3.9.2-slim-buster AS base

ARG APP_DIR=/usr/app/

USER root

RUN mkdir ${APP_DIR}

WORKDIR ${APP_DIR}

# pip requirements
COPY requirements.txt ${APP_DIR}

RUN pip install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "src/main.py"]