run:
	python3 main.py

build:
	docker build -t calculator .

run-docker: build
	docker run -it calculator

test: build
	docker run calculator python -m unittest discover .
