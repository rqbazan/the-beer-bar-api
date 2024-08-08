# The Beer Bar API

<p>
   <a href="https://www.python.org/downloads/release/python-3124/">
      <img alt="Python 3.12" src="https://img.shields.io/badge/python-3.12-blue.svg">
   </a>
   <a href="https://github.com/psf/black">
    <img alt="code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
   </a>
   <a href="https://microsoft.github.io/pyright/">
      <img alt="checked with pyright" src="https://microsoft.github.io/pyright/img/pyright_badge.svg">
   </a>
</p>

🍺 A simple REST API that allows to manage orders in a beer bar

## Decisions

I make some early design decisions, which are specified in the [docs/decisions](./docs/decisions) folder.

## Requirements

- Python >=3.12
- [Poetry](https://python-poetry.org/docs/) >=1.8

## Recommendations

- Use [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions. I made a little guide to install/use pyenv and Poetry, [maybe it can help you](https://rqbazan.notion.site/Hello-Python-c9627f7ad033471c9d52928b54b05eff?pvs=4).

- Config Poetry to create virtual env inside the project folder.

  ```bash
  poetry config virtualenvs.in-project true
  ```

## Getting started

1. Install dependencies:

   ```bash
   poetry install
   ```

2. Run for development:

   ```bash
   make dev
   ```

## Run tests

1. Run tests:

   ```bash
   make test:unit
   ```

## Deployment

This project is deployed on [fly.io](http://fly.io).

```
fly deploy
```

> **Note:** You need to have the [fly CLI](https://fly.io/docs/getting-started/installing-flyctl/) installed and be logged in.

## Other commands

| Command            | Description                    |
| ------------------ | ------------------------------ |
| `make test:static` | Run linter and formatter check |
| `make fix:format`  | Run formatter in all files     |

For more commands, please check the [Makefile](./Makefile).
