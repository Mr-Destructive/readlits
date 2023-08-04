.PHONY: local

local:
	gunicorn project.wsgi

