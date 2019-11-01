start:
	cd output/my_app && docker-compose up

build:
	# Recreates the cookiecutter project in a directory.
	rm -rf output
	mkdir -p output
	cd output && cookiecutter .. --no-input

teardown:
	docker-compose -f output/my_app/docker-compose.yml down -v
