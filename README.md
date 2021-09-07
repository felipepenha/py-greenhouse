![](/images/greenhouse_github_card_v02.png)

# py-greenhouse

A containerized Python framework for a better Data X development workflow. Where X = Science, Engineering, Analytics, etc.

The name "Greenhouse" is a metaphor. A greenhouse is a structure made of glass to grow plants despite of external conditions such as a cold winter. Likewise, the Greenhouse framework builds a standalone container for Rust developmet which is fully transparent to the user.

[Watch an overview clip on Twitch! 🖥️💜🖥️💜](https://www.twitch.tv/videos/1013368507)

![](/images/greenhouse_architecture_v03.png)


# But what is a template?

`py-greenhouse` is a GitHub template, not a package. This means that you will work on a copy of this project and you will replace placeholders by code that fits your own purposes.

If you just want to use the Greenhouse template for your new cool Data X or Machine Learning project, please choose the option ["Use this Template"](https://github.com/felipepenha/py-greenhouse/generate).

The current version of `py-greenhouse` uses the [Palmer Penguins dataset](https://github.com/mcnakhaee/palmerpenguins) called via an API (see [`src/data_sourcing.py`](https://github.com/felipepenha/py-greenhouse/blob/main/src/data_sourcing.py)). You may use other datasets, coming from different sources, and you may need to setup keys for cloud environment access, all of which are not covered here.


# Local OS Requirements

These are requirements for your local machine, ideally a Debian Linux OS:

## - [docker](https://docs.docker.com/engine/install/)

Follow the [instructions in the docker docs](https://docs.docker.com/engine/install/linux-postinstall/) to ensure that $USER has root access to docker.

## - [docker-compose](https://docs.docker.com/compose/install/)

## - VS Code

In your local machine:

1. [install VS Code](https://code.visualstudio.com/docs/setup/linux),

2. install the [`ms-vscode-remote.remote-containers`](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension locally,

A pop-up will open up asking if you would like to reload the workspace in the container:

![](/images/Screenshot_from_2021-03-07_18-31-36_VS-Code.png)

After choosing "Reopen in Container", VS Code will open the "bash" docker-compose service in the greenhouse container, as specified in the manifest `.devcontainer.json`. 

Notice that VS Code will run intilization commands that may take some time to process.

VS Code will already include the [`ms-python.python`](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension, without the need to install it in your own local machine. You may add any other extensions that you may need in your Python project in the configuration file `.devcontainer.json` .

## - [git](https://git-scm.com/download/linux)

```
sudo apt-get git
```

## - make

```
sudo apt-get update
sudo apt-get install build-essential
```

## - awk
## - tee
## - touch

## - python3

```
sudo apt-get update
sudo apt-get install python3
```

## - pip3

```
sudo apt-get update
sudo apt-get install python3-pip
```

## - pre-commit

```
pip3 install pre-commit
```

In the main directory of the project where there is already a `.git/` subdirectory:

```
pre-commit install
pre-commit migrate-config
pre-commit autoupdate
```

The main directory may be either the locally cloned py-greenhouse or a project based on the github template.

Alternatively, simply run in the terminal `make install-requirements`, to install the `pre-commit` Python package.

## - [dvc](https://dvc.org/doc/install/linux)

```
pip3 install dvc
```

## Do I need to install any other requirements?

No. After installing the basic local requirements described above, you are all set to run everything else inside a Docker container.

# Quick Start

This is a template repository. [Follow this link for instructions to create a repository from a template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template).


First, make sure `make`, `docker` and `docker-compose` are installed in your system.


The greenhouse dev work is performed via `make` commands.


To see the most up to date list of available commands run

```bash
$ make help

USAGE

    make <command>
    Include 'sudo' when necessary.
    To avoid using sudo, follow the steps in
    https://docs.docker.com/engine/install/linux-postinstall/


COMMANDS

    add-commit      git add, pre-commit, and commit
    bash            bash REPL (Read-Eval-Print loop), suitable for debugging
    build           build image using cache
    build-no-cache  build image from scratch, and not from cache
    docs            show the src modules documentation on the browser
    fastapi         starts up fastapi
    jupyter         access Python through the Jupyter Notebook
    pre-commit      early run of pre-commit git hooks
    python3         access Python through the REPL (Read-Eval-Print loop)
    release         release on dev branch. Be sure to update version.toml before running this operation
    run             run src/main.py
    test            run all tests using pytest (from within the container)

```


To build your greenhouse (as it is), you first need to run:

```bash
$ make build-no-cache
```


To access Jupyter in your local browser:

```bash
$ make jupyter

Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    
    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
    Or copy and paste one of these URLs:
        http://...:8888/lab?token=...
```


Next, you simply need to follow the instructions printed out on your own terminal.


In the generic example above, I would paste the following on my browser:

```bash
http://...:8888/lab?token=...
```


Any changes made in the files within the Jupyter interface, for example saved changes in `.rs`, `.ipynb`, and `.py` files, will be reflected in the original files you store locally, and vice-versa. This is ensured by the fact that the whole greenhouse directory is set as a `volume` in the `docker-compose.yml` configuration file.


You may also choose to run code using the REPL (Read-Eval-Print loop) in the terminal by running:

```bash
$ make python3
```


Now, you are ready to start developing Python code by creating new `.py` files in the `/src` directory.


During development phase, you can normally test out new code in a Jupyter Notebook.

Check out additional notebooks in the `/notebooks` directory (`.ipynb` files with preffix `example_`).


# Greenhouse Structure

```bash
.
├── conftest.py
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── notebooks
├── flow
├── images
├── LICENSE
├── logs
├── Makefile
├── monitor
├── README.md
├── requirements.txt
├── src
│   ├── data_preprocessing.py
│   ├── data_sourcing.py
│   ├── data_splitting.py
│   ├── eda_monitoring.py
│   ├── feature_engineering.py
│   ├── greenhouse_clock.py
│   ├── main.py
│   ├── modeling.py
│   ├── performance_monitoring.py
├── tests
│   ├── test_data_sourcing.py
│   ├── test_data_splitting.py
│   └── test_feature_engineering.py
└── version.toml
```

Highlights:

* `notebooks/`: notebooks, usually Jupyter Notebooks not in production
* `logs/`: dated logs, usually `.txt` files
* `monitor/`: files exported for monitoring purposes (data, model performance, etc). usually `.html` or `.json`.
* `flow/`: flow diagram as provided by `prefect`
* `requirements.txt`: pip3 requirements for your project
* `src/`: source directory for your Python project
* `src/main.py`: main file where flow is defined
* `test/`: tests of Python code. All tests will run automatically as pre-commit git hooks, in the container.
* `version.toml`: information about your project, such as the version number to be used in the git tag pushed to the repo with `make release`.



# Adding External Dependencies

You need to include any external dependencies to the `requirements.txt` file in addition to the default list provided here.


## Continuous Integration / Continuous Delivery (CI/CD)

Follow the instructins in [CONTRIBUTING.md](https://github.com/felipepenha/rust-greenhouse/blob/main/CONTRIBUTING.md). Be sure to update `version.toml` before each new release on the `dev` branch.

![](/images/greenhouse_architecture_gitops.png)
