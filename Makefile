SHELL := /bin/bash
export

.DEFAULT_GOAL := help

.PHONY: run
run:  ## run app
	poetry run uvicorn src.fastapi_score_server_app.bin.main:app --reload

.PHONY: format
format:  ## format and lint
	poetry run nox --session format
	poetry run nox --session lint

.PHONY: test
test:  ## test
	@echo "test"
	PYTHONPATH=./src poetry run pytest

.PHONY: codegen
codegen:  ## codegen from openapi specification
	poetry run datamodel-codegen \
		--input-file-type openapi \
		--input ./openapi/api.yml \
		--output ./src/fastapi_score_server_app/handler/schema.py

#########
# Utils #
#########

.PHONY: error
error:  ## errors処理を外部に記述することで好きなエラーメッセージをprintfで記述可能.
	$(error "${ERROR_MESSAGE}")

.PHONY: help
help:  ## show help
	@cat $(MAKEFILE_LIST) \
		| grep -E '^[.a-zA-Z0-9_-]+ *:.*##.*' \
		| xargs -I'<>' \
			bash -c "\
				printf '<>' | awk -F'[:]' '{ printf \"\033[36m%-15s\033[0m\", \$$1 }'; \
				printf '<>' | awk -F'[##]' '{ printf \"%s\n\", \$$3 }'; \
			"
