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

Create environment

```
pyenv install 3.5.1
cd python_projects
mkdir myproject
cd myproject
pyenv virtualenv 3.5.1 venv_myproject
```

Activate environment

```
pyenv activate venv_myproject
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


