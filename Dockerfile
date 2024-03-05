FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN apt update -y && \
    apt install -y gcc make automake && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/* && \
    apt-get clean && \
    adduser \
        --no-create-home \
        --shell /bin/bash \
        api-user

COPY ./app /app

# Create and set permissions for volumes
RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/logs && \
    chown -R api-user:api-user /vol && \
    chmod -R 755 /vol

EXPOSE 8080

ENV PATH="/py/bin:$PATH"

USER api-user


