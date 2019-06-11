CWD=$(shell pwd)
PKG=simple_calculator

clean:
	find ./$(PKG) -name "*.pyc" -exec rm -rfv {} \;

test:
	tox -r

.PHONY: test clean