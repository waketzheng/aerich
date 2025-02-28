checkfiles = aerich/ tests/ conftest.py
py_warn = PYTHONDEVMODE=1
MYSQL_HOST ?= "127.0.0.1"
MYSQL_PORT ?= 3306
MYSQL_PASS ?= "123456"
POSTGRES_HOST ?= "127.0.0.1"
POSTGRES_PORT ?= 5432
POSTGRES_PASS ?= 123456

up:
	@poetry update

deps:
	@poetry install --all-extras --all-groups

_style:
	@ruff format $(checkfiles)
	@ruff check --fix $(checkfiles)
style: deps _style

_check:
	@ruff format --check $(checkfiles) || (echo "Please run 'make style' to auto-fix style issues" && false)
	@ruff check $(checkfiles)
	@mypy $(checkfiles)
	@bandit -r aerich
check: deps _check

_lint:
	ruff format $(checkfiles)
	ruff check --fix $(checkfiles)
	mypy $(checkfiles)
	bandit -c pyproject.toml -r aerich
	@poetry build
	twine check dist/*
lint: deps _lint

test: deps
	$(py_warn) TEST_DB=sqlite://:memory: pytest

test_sqlite:
	$(py_warn) TEST_DB=sqlite://:memory: pytest

test_mysql:
	$(py_warn) TEST_DB="mysql://root:$(MYSQL_PASS)@$(MYSQL_HOST):$(MYSQL_PORT)/test_\{\}" pytest -vv -s

test_postgres:
	$(py_warn) TEST_DB="postgres://postgres:$(POSTGRES_PASS)@$(POSTGRES_HOST):$(POSTGRES_PORT)/test_\{\}" pytest -vv -s

test_psycopg:
	$(py_warn) TEST_DB="psycopg://postgres:$(POSTGRES_PASS)@$(POSTGRES_HOST):$(POSTGRES_PORT)/test_\{\}" pytest -vv -s

_testall: test_sqlite test_postgres test_mysql
testall: deps _testall

build: deps
	@poetry build

ci: build _check _testall
