.PHONY: test

test:
	PYTHONPATH=$$(pwd)/monty pytest .

