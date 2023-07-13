ignores        := .gitkeep Makefile
python_version := 3.10


run: format
	@python${python_version} ./src/lambda_function.py

format:
	@isort ./src \
	&& black ./src \
	&& ruff ./src \
	&& npx prettier --write .

package: packages-clean
	@make python_version="${python_version}" -C packages/

packages-clean:
	@find packages -mindepth 1 $(foreach i, $(ignores), ! -name $(i)) \
	| grep -v "/\." \
	| xargs rm -rf

docs-clean:
	@find docs -mindepth 1 $(foreach i, $(ignores), ! -name $(i)) \
	| grep -v "/\." \
	| xargs rm -rf

update:
	@make build \
	&& make copy \
	&& make format

build: docs
	@sphinx-build ./docs_src/ ./docs_src/_build/

nojekyll:
	@touch ./docs/.nojekyll

install:
	@python${python_version} -m pip install -r requirements.txt

docs: packages-clean
	@sphinx-apidoc -f -o ./docs_src .

copy:
	@cp -rp ./docs_src/_build/* ./docs

.PHONY: docs
