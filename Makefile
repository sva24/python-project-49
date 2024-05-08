# Makefile
install: #  установка poetry
	poetry install

brain-games: # запустить проект
	poetry run brain-games

build: # билд)
	poetry build

publish: #  отладка публикаций без добавления в каталог PyPI
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl

