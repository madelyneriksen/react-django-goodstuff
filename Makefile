rebuild:
	# Recreates the cookiecutter project in a directory.
	rm -rf output
	mkdir -p output
	cd output && cookiecutter .. --no-input
