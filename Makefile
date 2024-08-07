freeze:
	uv pip freeze | uv pip compile - -o requirements.txt

sync:
	uv pip sync requirements.txt

venv:
	source .venv/bin/activate


