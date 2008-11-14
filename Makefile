# Makefile for Nosy package

# Author: Doug Latornell
# Created: 2008-11-10

.PHONY: all docs clean

all: docs egg

docs:
	buildhtml.py docs

egg:	nosy/nosy.py
	python setup.py bdist_egg

clean:
	-rm -f docs/index.html
	-rm -rf dist build Nosy.egg-info

# end of file
