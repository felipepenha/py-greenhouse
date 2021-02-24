FROM python:3.9.2-alpine3.13 AS base

ARG APP_DIR=/usr/app/

USER root

RUN mkdir ${APP_DIR}

WORKDIR ${APP_DIR}

RUN apk update

RUN apk add --update alpine-sdk

RUN apk add py-pip

COPY requirements.txt ${APP_DIR}

RUN pip install -r requirements.txt
