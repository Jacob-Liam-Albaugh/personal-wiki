N ?= 2

all: authors refs graph

authors:
	python3 tools/authors.py

refs:
	python3 tools/refs.py --n $(N)

graph:
	uv tool run --from graphifyy python -I tools/graph.py .

test:
	cd tools && python3 test_tools.py

.PHONY: all authors refs graph test
