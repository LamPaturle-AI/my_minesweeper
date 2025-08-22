FROM python:3.10-slim

RUN pip install poetry==2.1.4

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PATH="/my_minesweeper/.venv/bin:$PATH"

WORKDIR /my_minesweeper

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

RUN poetry install --without dev

EXPOSE 80

ENTRYPOINT ["poetry", "run", "python", "-m", "app/app.py"]
