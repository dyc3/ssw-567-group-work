default:
    just --list

lint:
    poetry run black --check .
    poetry run mypy .

format:
    just --unstable --fmt
    poetry run black .

test:
    poetry run coverage run --branch -m pytest
    poetry run coverage report -m
