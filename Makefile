.PHONY: all zip clean fix mypy pylint ankiweb vendor serve

all: zip

zip:
	python -m ankibuild --type package --qt all --noconsts --forms-dir forms --exclude user_files/**/

ankiweb:
	python -m ankibuild --type ankiweb --qt all --noconsts --forms-dir forms --exclude user_files/**/

fix:
	python -m black --exclude="ankidata" src
	python -m isort src

mypy:
	python -m mypy src

pylint:
	python -m pylint src

clean:
	rm -rf build/
