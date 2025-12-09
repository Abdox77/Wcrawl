.PHONY: run install clean

run:
	python main.py

install:
	pip install beautifulsoup4 requests lxml

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
