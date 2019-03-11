test:
	@which pycodestyle && pycodestyle solutions.py || true
	python3 -tt test.py


clean:
	find . -type d -name __pycache__ | xargs rm -vrf
