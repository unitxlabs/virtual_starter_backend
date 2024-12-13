# Stage 1: Build stage
FROM python:3.11-slim as build

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt cython setuptools numpy alembic

COPY . .

RUN python setup.py build_ext --inplace


# Stage 2
FROM python:3.11

ARG RUNTIME_ENV=production

RUN mkdir /app


ENV LANG=C.UTF-8 \
  LC_ALL=C.UTF-8

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl \
  && rm -rf /var/lib/apt/lists/* \

COPY requirements.txt requirements_test.txt.
COPY ./scripts/entrypoint.sh ./scripts/start.sh /

RUN pip install --no-cache-dir -r requirements.txt

RUN if [ "$RUNTIME_ENV" = "test" ]; then \
        echo "Installing test dependencies..." && \
        pip install --no-cache-dir -r requirements-test.txt; \
    fi

COPY --from=build /app /app

WORKDIR /app