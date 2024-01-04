# PyEnv

## Installation

### MacOs

Install with HomeBrew

```
brew install pyenv
brew install pyenv-virtualenv
```

Setup .zshrc

```
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Ubuntu


### Windows



## Usage

List possible installs

```
pyenv install --list
```

List environments

```
pyenv versions
```

Install python version

```
pyenv install <version>
```

Create environment

```
pyenv virtualenv <version> <venv-name>
```

Activate environment

```
pyenv activate <venv-name>
```

Install requirements.txt

```
pip install -r requirements.txt
```

Create requirements.txt

```
pip freeze > requirements.txt
```

Remove environment

```
pyenv virtualenv-delete <venv-name>
```


