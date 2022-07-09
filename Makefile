.PHONY: tests docs

test:
	poetry run pytest -vvv

docs:
	PYTHONPATH=. poetry run mkdocs build && mkdocs gh-deploy
