![](/images/py-greenhouse_github_card.png)

# py-greenhouse
A containerized Python framework for a better Data X development workflow. Where X = Science, Engineering, Analytics, etc.

# Local Requirements

These are requirements for your local machine, ideally Linux OS:

### [docker](https://docs.docker.com/engine/install/)

### [docker-compose](https://docs.docker.com/compose/install/)

### VS Code

In your local machine:

1. [install VS Code](https://code.visualstudio.com/docs/setup/linux),

2. install the [`ms-vscode-remote.remote-containers`](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension locally,

3. follow the [instructions in the docker docs](https://docs.docker.com/engine/install/linux-postinstall/) to ensure that $USER has root access to docker.

The next time you open up VS Code in the project directory, VS Code should already be running in the greenhouse container, as specified in the manifest `.devcontainer.json`. 

Notice that VS Code will run intilization commands that may take some time to process.

VS Code will already include the [`ms-python.python`](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension, without the need to install it in your own local machine.

### [git](https://git-scm.com/download/linux)

### make

Installation (Debian):

```
sudo apt-get update
sudo apt-get install build-essential
```

### python3


Installation (Debian):

```
sudo apt-get update
sudo apt-get install python3
```

### pip3

Installation (Debian):

```
sudo apt-get update
sudo apt-get install python3-pip
```

### pre-commit

```
pip3 install pre-commit
pre-commit install
pre-commit migrate-config
pre-commit autoupdate
```

Or, simply run `make install-requirements`.

# To Do

1. Dockerfile to define container
2. Docker-compose with services
3. VS Code integration with Docker
4. Makefile with definitions of commands, e.g. `make release`
5. Git hooks
    * [linting](https://medium.com/staqu-dev-logs/keeping-python-code-clean-with-pre-commit-hooks-black-flake8-and-isort-cac8b01e0ea1)
    * testing (pytest)
6. Python Template for the Machine Learning Pipeline
    * Reading Data
    * Data Cleansing
    * Feature Engineering
    * Exploratory Data Analysis
    * Model Development
    * Performance Monitoring (logs)
    * Model Interpretation (SHAP)
7. Model Versioning, e.g. MLFlow, DVC, CML
8. API