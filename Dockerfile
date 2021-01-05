FROM python:3.9-alpine

ENV \
    PATH=/opt/local/bin:$PATH \
    PYTHONPATH=/app/ \
    PYTHONUNBUFFERED=1 \
    FAST_APP=$FAST_APP \
    APP_ENV=$APP_ENV \
    APP_VERSION=$APP_VERSION \
    DB_HOSTNAME=$DB_HOSTNAME \
    DB_PORT=$DB_PORT \
    DB_NAME=$DB_NAME \
    DB_USERNAME=$DB_USERNAME \
    DB_PASSWORD=$DB_PASSWORD \
    SQLALCHEMY_POOL_SIZE=$SQLALCHEMY_POOL_SIZE \
    SQLALCHEMY_MAX_OVERFLOW=$SQLALCHEMY_MAX_OVERFLOW



RUN mkdir /app
ADD requirements.txt $EXTRA_REQUIREMENTS /app/
WORKDIR /app


RUN apk --no-cache add -U \
    libpq \
    bash \
    curl \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    make \
    libffi-dev\
    postgresql-dev 


RUN pip install -r /app/${EXTRA_REQUIREMENTS:-requirements.txt}

RUN apk --purge --no-cache del .build-deps \
    && rm -rf /var/cache/apk/*

ADD . /app/

EXPOSE 8000

COPY /bin/boot.sh /

RUN ["chmod", "+x", "/boot.sh"]

ENTRYPOINT [ "/boot.sh" ]
