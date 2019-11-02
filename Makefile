test: teardown
	# Recreates the cookiecutter project in a directory.
	rm -rf output
	mkdir -p output
	cd output && cookiecutter .. --no-input
	cd {{cookiecutter.project_package}} && black . --check

teardown:
	docker-compose -f output/my_app/docker-compose.yml down -v || echo "Already Dead!"

start:
	cd output/my_app && docker-compose up
