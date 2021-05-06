# Contributing

These contributing guidelines were designed both for the original [Greenhouse repo template](https://github.com/felipepenha/py-greenhouse) and any Python projects derived from that template.

If you just want to use the Greenhouse template for your new cool Data X or Machine Learning project, please choose the option ["Use this Template"](https://github.com/felipepenha/py-greenhouse/generate).

# Bugs, questions, or suggestions

In case you found bugs, would like to ask a question, or have suggestions to offer, feel free to use the [Issues Section](https://github.com/felipepenha/py-greenhouse/issues) in the GitHub repository.


# New Features and/or improvements


## Cloning

Clone the repository locally:

```git
$ git clone https://github.com/felipepenha/py-greenhouse.git
$ git pull dev
$ git branch dev
```

Start working on a new branch copied from the `dev` branch:

```git
$ git checkout -b [new_branch_name]
$ git branch --set-upstream-to=origin/dev [new_branch_name]
```


## Adding and Commiting

Use `git add [target]` and `git commit -m [message]` normally, at this point. Every time you commit, pre-commit hooks are triggered and your code will be linted and tested. If it fails on the first pass, you will need to git add again and commit.

Alternatively, run `make add-commit` (see also [issue #17](https://github.com/felipepenha/py-greenhouse/issues/17)).


## Dealing With Inconsistencies

In case you new branch gets behind `dev`, you may correct it by performing

```git
$ git stash save
$ git pull [new_branch_name]
$ git stash pop
```

You may have to deal with the inconsistencies that may arise from that process before proceeding.

If you want to make your branch available online:

```git
$ git push origin [new_branch_name]
```


## New Releases

Instructions for a new release:

1. Check which is the latest version (Ex: `0.0.1`);
2. Change the field `version` in `version.toml` (Ex: `version="0.0.2"`);
3. Add your name and email address to the field `authors` in `version.toml`; and
4. Run:
```bash
$ make release
```

The above command will take care of checking the version in `version.toml` and releasing your code on `dev` with a tag consistent with `version.toml`.

## Pull Requests to the Main Branch

New releases will usually be pulled/merged to `main` and need approval.

# Conventions

## Commit Messages

[conventionalcommits.org v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)

Some common commit messages you will find in the project:

```git
"docs:"
"fix:"
"feat:"
"refactor:"
"test:"
```


## Versioning

[Semantic Versioning 2.0.0](https://semver.org/)

## Docstrings

[Numpy Docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)

A useful template:

```python
def func(x):
    """[Summary]

    Parameters
    ----------
    x: type
        [description]

    Returns
    -------
    type
        [description]

    Examples
    --------

    Raises
    ------

    Notes
    -----

    """
```