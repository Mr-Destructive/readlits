.PHONY: local

local:
	gunicorn project.wsgi

coverage:
	pytest --cov=readlits --migrations -n 2 --dist loadfile

fcov:
	@pytest --cov=readlits -n 4 --dist loadfile
