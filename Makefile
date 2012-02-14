# Makefile for Nosy package

# Author: Doug Latornell

.PHONY: all docs clean

all: docs sdist

docs:	docs/index.txt
	(cd docs && \
	rst2html.py --title="Nosy Reloaded" --generator --date \
		index.txt index.html)

sdist:	nosy/nosy.py
	python setup.py sdist

clean:
	-rm -f docs/index.html
	-rm -rf dist build Nosy.egg-info
