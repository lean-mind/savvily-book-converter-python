.DEFAULT_GOAL := help


.PHONY: help
help:
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pipenv install --dev

.PHONY: tests
tests: _check-output ## Run all tests with coverage
	@pipenv run pytest --cov=src

.PHONY: tests-watch
tests-watch: _check-output ## Run all tests in watch mode
	@pipenv run ptw

.PHONY: tests-ci
tests-ci: ## Run all tests forcing book compilation
	@pipenv install --dev
	./convert.sh -a
	@pipenv run tests

.PHONY: check-output
_check-output:
	@echo "Checking output"
	@test -s output || { echo "No output found, compiling all formats..."; ./convert.sh -a; }
	@test -s output/ebook.epub || { echo "No epub found, compiling ..."; ./convert.sh -e; }
	@test -s output/python_print.pdf || { echo "No print pdf found, compiling ..."; ./convert.sh -p; }
	@test -s output/python_screen.pdf || { echo "No screen pdf found, compiling ..."; ./convert.sh -s; }
