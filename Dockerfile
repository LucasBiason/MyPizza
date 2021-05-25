FROM python:3.8-slim

LABEL maintainer="Lucas Biason lucas.biason@foxcodesoftware.com"
LABEL application="msstizza"

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=src.settings

RUN apt-get update
COPY build/. .
RUN chmod +x ./entrypoint.sh
RUN bash linux-requirements.sh

RUN pip install pip setuptools --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

COPY app .

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
