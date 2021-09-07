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
MAKEFILE_ABS_PATH = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

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
	@echo "    add-commit      git add, pre-commit, and commit"
	@echo "    bash            bash REPL (Read-Eval-Print loop), suitable for debugging"
	@echo "    build           build image using cache"
	@echo "    build-no-cache  build image from scratch, and not from cache"
	@echo "    docs            show the src modules documentation on the browser"
	@echo "    dvc             runs dvc commands for model versioning and comparison"
	@echo "    fastapi         starts up fastapi"
	@echo "    jupyter         access Python through the Jupyter Notebook"
	@echo "    palmer-penguins moves files in examples/palmer_penguins to the main dir"
	@echo "    pre-commit      early run of pre-commit git hooks"
	@echo "    python3         access Python through the REPL (Read-Eval-Print loop)"
	@echo "    release         release on dev branch. \
	Be sure to update version.toml before running this operation"
	@echo "    run             run src/main.py"
	@echo "    vanilla         moves files in examples/vanilla to the main dir"
	@echo "    test            run all tests using pytest (from within the container)"
	@echo "    test-no-log     same as test but without log generation"

#################
# User Commands #
#################

build:
	mkdir --parents monitor
	mkdir --parents logs
	mkdir --parent models
	$(BUILD)

build-no-cache:
	mkdir --parents monitor
	mkdir --parents logs
	$(BUILD) --no-cache

bash:
	$(RUN) bash

python3:
	$(RUN) python3

jupyter:
	$(RUN) --service-ports jupyter

fastapi:
	$(RUN) --service-ports fastapi

test-no-log:
	$(RUN) test

test:
	# test and append log to file including datetime in UTC
	(date --utc && $(RUN) test) 2>&1 | tee -ai logs/log_test.txt

run:
	# run and append log to file including datetime in UTC
	(date --utc && $(RUN) run) 2>&1 | tee -ai logs/log_run.txt

pre-commit:
	pre-commit run --all-files

dvc:
	- dvc checkout
	# DVC pipeline
	- dvc repro
	# Trigger dvc metrics diff file logging
	# $(compare-to) is the git rev you are comparing to
	dvc metrics diff --all $(compare-to) > logs/log_metrics_diff.txt

add-commit:
	# `-` signalizes that errors will be ignored by make
	# Add all files in the current directory
	- git add .
	# Run hooks in `pre-commit` that cause file changes
	- pre-commit run check-toml
	- pre-commit run check-yaml
	- pre-commit run pretty-format-json
	- pre-commit run requirements-txt-fixer
	- pre-commit run black
	- pre-commit run flake8
	# Add currently tracked files (which have been modified)
	- git add --update
	# Commit with `--message "$(message)"`.
	# `pre-commit` will run once again,
	# but now for all hooks
	git commit --message="$(message)"

release:
	# Create tag based on `version.toml`
	# `-` signalizes that errors will be ignored by make
	git tag --annotate $(VERSION) \
	--message "VERSION=$(VERSION) read from `version.toml`"
	# Push from `HEAD` (on current branch) to `dev`,
	# using the tag created above.
	# Append log to file including datetime in UTC
	(date --utc && git push origin HEAD:dev tag $(VERSION)) \
	2>&1 | tee -ai logs/log_release.txt

docs:
	# Auto documentation.
	# references: https://pdoc.dev/ | https://calmcode.io/makefiles/phony-folders.html
	$(RUN) --service-ports docs

vanilla:
	echo ""
	echo "COPYING FROM $(MAKEFILE_ABS_PATH)/examples/vanilla/** TO $(MAKEFILE_ABS_PATH)"
	echo ""
	cp -r $(MAKEFILE_ABS_PATH)/examples/vanilla/** $(MAKEFILE_ABS_PATH)

palmer-penguins:
	echo ""
	echo "COPYING FROM $(MAKEFILE_ABS_PATH)/examples/palmer_penguins/** TO $(MAKEFILE_ABS_PATH)"
	echo ""
	cp -r $(MAKEFILE_ABS_PATH)/examples/palmer_penguins/** $(MAKEFILE_ABS_PATH)
