FROM python:slim AS base

USER root

RUN mkdir /usr/app

WORKDIR /usr/app