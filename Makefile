# The present file, 'Makefile' has been modified from the original at
# https://github.com/NeowayLabs/data-science-template
# under the folllowing license:
#
# MIT License
#
# Copyright (c) 2019 Neoway Business Solution
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

BUILD = docker-compose build
RUN = docker-compose run
VERSION = $(shell awk -F ' = ' '$$1 ~ /version/ { gsub(/[\"]/, "", $$2); printf("%s",$$2) }' version.toml)

help:
	@echo "USAGE"
	@echo
	@echo "    make <command>"
	@echo "    Include 'sudo' when necessary."
	@echo "    To avoid using sudo, follow the steps in"
	@echo "    https://docs.docker.com/engine/install/linux-postinstall/"
	@echo
	@echo
	@echo "COMMANDS"
	@echo
	@echo "    build           build image using cache"
	@echo "    build-no-cache  build image from scratch, and not from cache"
	@echo "    bash            bash REPL (Read-Eval-Print loop), suitable for debugging"
	@echo "    python3         access Python through the REPL (Read-Eval-Print loop)"
	@echo "    jupyter         access Python through the Jupyter Notebook"
	@echo "    release         Release on the dev branch"

#################
# User Commands #
#################

install-requirements:
	pip3 install pre-commit
	pre-commit install
	pre-commit migrate-config
	pre-commit autoupdate

build:
	$(BUILD)

build-no-cache:
	$(BUILD) --no-cache

bash:
	$(RUN) bash

python3:
	$(RUN) python3

jupyter:
	$(RUN) --service-ports jupyter

test:
	$(RUN) test

debug:
	echo $(VERSION)

release:
	git tag -a $(VERSION) -m "VERSION=$(VERSION) read from `version.toml`"
	git push origin HEAD:dev tag $(VERSION)