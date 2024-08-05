# The Beer Bar API

🍺 A simple REST API that allows to manage orders in a beer bar

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

2. Enter to the virtual env:

   ```bash
   poetry shell
   ```

3. Run for development:

   ```bash
   make dev
   ```

## Run tests

1. Enter to the virtual env (if you are not in it):

   ```bash
   poetry shell
   ```

2. Run tests:

   ```bash
   make test
   ```

## Deployment

This project is deployed on [fly.io](http://fly.io).

```
fly deploy
```

> **Note:** You need to have the [fly CLI](https://fly.io/docs/getting-started/installing-flyctl/) installed and be logged in.
