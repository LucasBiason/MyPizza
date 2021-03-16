FROM python:3.8-slim

LABEL maintainer="Lucas Biason lucas.biason@foxcodesoftware.com"
LABEL application="msstizza"

ENV HOME=/home/lucas

RUN addgroup lucas && \
    adduser -D -h ${HOME} -G lucas lucas && \
    mkdir -p /root/.ssh && \
    mkdir -p ${HOME}/logs

ONBUILD RUN apt-get update
ONBUILD COPY build/linux-requirements.sh .
ONBUILD RUN bash linux-requirements.sh

ONBUILD RUN pip install pip setuptools --no-cache-dir

ONBUILD COPY build/requirements.txt .
ONBUILD RUN pip install -r requirements.txt --no-cache-dir

ONBUILD COPY src src
ONBUILD COPY manage.py .
ONBUILD COPY wsgi.py .

WORKDIR ${HOME}

EXPOSE 5000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000" ]
