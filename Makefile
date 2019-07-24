CWD=$(shell pwd)
PKG=simplecalc

clean:
	find ./$(PKG) -name "*.pyc" -exec rm -rfv {} \;

test:
	tox -r

.PHONY: test clean