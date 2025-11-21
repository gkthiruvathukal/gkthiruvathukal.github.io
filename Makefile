build_project:
	git describe --tags --abbrev=0 | tail -n 1 | xargs -I % uv version %
	rm -rf dist/
	uv build
	uv pip install dist/*.tar.gz
	sphinx-build -vvv --write-all --fresh-env src build

create-dev:
	pre-commit install
	pre-commit autoupdate
	uv sync
	uv build

serve:
	python -m http.server -d build 12300
