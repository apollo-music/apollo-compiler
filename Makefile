all:
	pip3 install -r ./src/requirements.txt && coverage run ./src/test.py && coverage report