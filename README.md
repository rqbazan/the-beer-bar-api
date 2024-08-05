# The Beer Bar API

This is a simple REST API that allows to manage orders in a beer bar.

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
