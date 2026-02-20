# CI/CD Learning Project

A simple Python calculator project used to learn Git CI/CD with GitLab Pipelines.

## Project Structure

```
cicd/
├── calculator.py        # Python script with add, subtract, multiply, divide
├── test_calculator.py   # pytest test cases
└── .gitlab-ci.yml       # GitLab CI/CD pipeline config
```

## What It Does

The pipeline runs automatically on every `git push` and has two stages:

1. **lint** — checks code style using `flake8`
2. **test** — runs 5 automated tests using `pytest`

If lint fails, tests are skipped. If tests fail, the pipeline goes red.

## Run Tests Locally

```bash
pip install pytest flake8

# run tests
pytest test_calculator.py -v

# run lint
flake8 calculator.py
```

## Pipeline

| Stage | Tool    | What it checks              |
|-------|---------|-----------------------------|
| lint  | flake8  | Code style and formatting   |
| test  | pytest  | Correctness of all functions|
