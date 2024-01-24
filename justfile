default:
    just --list

lint:
    poetry run black --check .
    poetry run mypy .

format:
    just --unstable --fmt
    poetry run black .

test:
    poetry run pytest
