FROM python:3.12

WORKDIR /usr/local/app

COPY poetry.lock pyproject.toml alembic.ini ./
COPY src ./src

ENV POETRY_HOME="/usr/local" \
    POETRY_VERSION="1.8.3" \
    POETRY_VIRTUALENVS_IN_PROJECT="true" \
    UVICORN_HOST="0.0.0.0"

ENV PATH=$POETRY_HOME/bin:$PATH

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry install --no-interaction

EXPOSE 8000

RUN useradd app
USER app

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "src.main:app"]
