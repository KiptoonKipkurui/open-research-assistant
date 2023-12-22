PYLINT = pylint
PYLINTFLAGS = -rn
PYTHONFILES := $(git ls-files *.py)

# pylint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

# %.pylint:
#     $(PYLINT) $(PYLINTFLAGS) $*.py

.PHONY: test
# runs unit tests
test:
	python3 -m unittest discover -s . -p '*_test.py'

# .PHONY: lint
# # Run linting tests
# lint:
# 	$(PYLINT) $(git ls-files '*.py')

.PHONY: list
list:
	echo $(PYTHONFILES)

.PHONY: up down venv check-deps update-deps install-deps isort black mypy flake8 bandit lint test migrate serve

ifneq (,$(wildcard ./env))
    include env
    export
endif

VENV=env
PYTHON=$(VENV)/bin/python3

cmd-exists-%:
	@hash $(*) > /dev/null 2>&1 || \
		(echo "ERROR: '$(*)' must be installed and available on your PATH."; exit 1)

up:  ## Run Docker Compose services
	docker-compose -f docker-compose.local.yml up -d

down:  ## Shutdown Docker Compose services
	docker-compose -f docker-compose.local.yml down

venv: requirements-dev.txt Makefile
	python3 -m pip install --upgrade pip setuptools wheel
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements-dev.txt

check-deps:  ## Check new versions and update deps
	$(PYTHON) -m pur -r requirements-dev.txt -d

update-deps:  ## Check new versions and update deps
	$(PYTHON) -m pur -r requirements-dev.txt

install-deps:  ## Install dependencies
	$(PYTHON) -m pip install -r requirements-dev.txt

isort:
	$(PYTHON) -m isort --skip env .

black:
	$(PYTHON) -m black --check .

mypy:
	$(PYTHON) -m mypy .

flake8:
	$(PYTHON) -m flake8 --exclude env .

bandit:
	$(PYTHON) -m bandit --exclude env -r .

lint: isort black mypy flake8 bandit

serve:  ## Run application server in development
	$(PYTHON) main.py

.PHONY: clean
# clean the project by removing build files
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf `find . -type d -name '*.egg-info' `
	rm -rf `find . -type d -name 'pip-wheel-metadata' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build

.PHONY: run
# Sets up the virtual environment, installs the dependencies and runs the project
run: venv 
	uvicorn main:app 