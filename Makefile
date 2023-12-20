.PHONY: test
# runs unit tests
test:
	python3 -m unittest discover -s . -p '*_test.py'