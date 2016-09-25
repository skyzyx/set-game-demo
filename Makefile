all:
	@cat Makefile | grep : | grep -v PHONY | grep -v @ | sed 's/:/ /' | awk '{print $$1}' | sort

#-------------------------------------------------------------------------------

.PHONY: lint
lint:
	autopep8 --max-line-length 120 --in-place set_game_demo/*.py
	autoflake --in-place --remove-unused-variables set_game_demo/*.py
	pylint --rcfile .pylint set_game_demo/
	pylint --rcfile .pylint tests/*.py --disable F0401

.PHONY: test
test:
	pip install -e .
	nose2

#-------------------------------------------------------------------------------

.PHONY: docs
docs:
	pdoc --html --html-dir docs --overwrite --all-submodules --external-links set_game_demo

.PHONY: pushdocs
pushdocs: docs
	rm -Rf /tmp/gh-pages
	git clone git@github.com:skyzyx/set-game-demo.git --branch gh-pages --single-branch /tmp/gh-pages
	cp -Rf ./docs/set_game_demo/* /tmp/gh-pages/
	cd /tmp/gh-pages/ && git add . && git commit -a -m "Automated commit on $$(date)" && git push origin gh-pages

#-------------------------------------------------------------------------------

.PHONY: readme
readme:
	pandoc -r markdown_github -w rst -o README.rst README.md

.PHONY: buildpip
buildpip: clean
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: pushpip
pushpip: buildpip
	twine upload dist/*

.PHONY: tag
tag:
	@ if [ $$(git status -s -uall | wc -l) != 0 ]; then echo 'ERROR: Git workspace must be clean.'; exit 1; fi;

	@echo "This release will be tagged as: $$(cat ./VERSION)"
	@echo "This version should match your package. If it doesn't, re-run 'make buildpip'."
	@echo "---------------------------------------------------------------------"
	@read -p "Press any key to continue, or press Control+C to cancel. " x;

	chag update $$(cat ./VERSION)
	git add .
	git commit -S -a -m "Preparing the $$(cat ./VERSION) release."
	chag tag $$(cat ./VERSION)

#-------------------------------------------------------------------------------

.PHONY: version
version:
	@echo "Current version: $$(cat ./VERSION)"
	@read -p "Enter new version number: " nv; \
	printf "$$nv" > ./VERSION

.PHONY: clean
clean:
	rm -Rf **/*.pyc **/__pycache__ build/ dist/ docs/ *.egg-info/
