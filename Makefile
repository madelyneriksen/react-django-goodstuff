test: teardown
	# Recreates the cookiecutter project in a directory.
	rm -rf output
	mkdir -p output
	cd output && cookiecutter .. --no-input
	cd output/my_app && make build
	cd output/my_app && make test

teardown:
	docker-compose -f output/my_app/docker/docker-compose.yml down -v || echo "Already Dead!"

start:
	cd output/my_app && make start
