## base image
FROM python:3.9.6-slim-buster AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc



## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"




## add and install requirements
RUN pip install --upgrade pip && pip install pip-tools
COPY requirements.txt .
RUN pip install -r requirements.txt



FROM python:3.9.6-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv
## set working directory
WORKDIR /usr/src/app

## add user
RUN addgroup --system user && adduser --system --no-create-home --group user
RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app


## switch to non-root user
USER user

## add app
COPY server/app/ ./.env ./


## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"


EXPOSE 8080

RUN pip install gunicorn

RUN ls -la

## run server
CMD [ "gunicorn", "-w", "1", "--bind", "0.0.0.0:8080", "wsgi:app"]
