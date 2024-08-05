FROM python:3.12-bookworm AS builder
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml poetry.lock ./
RUN poetry install

FROM python:3.12-slim-bookworm AS runner
WORKDIR /app
COPY --from=builder /app/.venv .venv/
COPY . .
EXPOSE 8000
CMD [".venv/bin/uvicorn", "main:app", "--app-dir", "./src", "--host", "0.0.0.0", "--port", "8000"]
