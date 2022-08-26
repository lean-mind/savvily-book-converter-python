.DEFAULT_GOAL := help


.PHONY: help
help:
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pipenv install --dev

.PHONY: check-types
check-types: ## Setup local environment
	@pipenv run mypy src

.PHONY: tests
tests: _check-output ## Run all tests
	@pipenv run pytest

.PHONY: tests-c
tests-c: _check-output ## Run all tests with coverage
	@pipenv run pytest --cov=src

.PHONY: tests-w
tests-w: ## Run domain and infrastructure tests in watch mode
	@pipenv run ptw --ignore tests/pandoc_integration

.PHONY: check-output
_check-output:
	@echo "Checking output"
	@test -s output || { echo "No output found, compiling all formats..."; ./convert.sh -a './tests/pandoc_integration/fixtures/sample-manuscript/'; }
	@test -s output/ebook.epub || { echo "No epub found, compiling ..."; ./convert.sh -e './tests/pandoc_integration/fixtures/sample-manuscript/'; }
	@test -s output/python_print.pdf || { echo "No print pdf found, compiling ..."; ./convert.sh -p './tests/pandoc_integration/fixtures/sample-manuscript/'; }
	@test -s output/python_screen.pdf || { echo "No screen pdf found, compiling ..."; ./convert.sh -s './tests/pandoc_integration/fixtures/sample-manuscript/'; }
