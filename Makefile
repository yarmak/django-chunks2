clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

makemessages:
	cd demo && python manage.py makemessages --all --no-location --symlinks

compilemessages:
	cd demo && python manage.py compilemessages

release: clean
	python setup.py register sdist upload --sign
	python setup.py bdist_wheel upload --sign
