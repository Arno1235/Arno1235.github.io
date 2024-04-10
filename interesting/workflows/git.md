# Git

## Installation

### MacOS

Install with HomeBrew

```
brew install git
```

## Usage

Clone

```
gh repo clone Arno1235/...
```

Push change

```
git add .
git commit -m <commit-mmesage>
git push
```

Git switch branch

```
git fetch origin
git checkout <branch-name>
```

Git pull rebase

```
git pull --rebase
```

Git force pull

```
git fetch --all
git reset --hard origin/master
```

Git force push

```
git push --force
```

Soft Reset: If you want to keep the changes from your commits but undo the commits themselves, you can perform a soft reset. This will move the HEAD pointer to a previous commit, effectively "undoing" the commits but leaving your changes staged. (Replace n with the number of commits you want to go back. For example, git reset --soft HEAD~1 will undo the last commit.)

```
git reset --soft HEAD~n
```

Mixed Reset: This is similar to a soft reset, but it also unstages your changes. Your changes will still be present in your working directory, but they won't be staged for commit. This will keep your changes in the working directory but remove them from the staging area. You can then selectively add the changes you want to commit.

```
git reset --mixed HEAD~n
```

Remove files that are in the gitignore

```
git rm -r --cached . # We remove
git add . # We stage
git commit -m "Clean up ignored files"
```
