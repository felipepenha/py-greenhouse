# Contributing

These contributing guidelines were designed both for the original [Greenhouse repo template](https://github.com/felipepenha/rust-greenhouse) and any Python packages derived from that template.


## Bugs, questions, or suggestions


In case you found bugs, would like to ask a question, or have suggestions to offer, feel free to use the [Issues Section](https://github.com/felipepenha/py-greenhouse/issues) in the GitHub repository.


## New Features and/or improvements


Clone the repository locally:

```git
$ git clone https://github.com/felipepenha/py-greenhouse.git
$ git pull dev
$ git branch dev
```


Start working on a new branch copied from the `dev` branch:

```git
$ git branch -b [new_branch_name]
$ git branch --set-upstream-to=origin/dev [new_branch_name]
```

Use `git add [target]` and `git commit -m [message]` normally, at this point.

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

Now, in order to release your branch on `dev`, you must follow the following steps:

1. Check which is the latest version (Ex: `0.1.0`);
2. Change the field `version` in `version.toml` (Ex: `version="0.1.1"`);
3. Add your name and email address to the field `authors` in `version.toml`; and
4. Run:
```bash
$ make release
```

The above command will take care of checking the version in `version.toml` and releasing your code on `dev` with a tag consistent with `version.toml`.

