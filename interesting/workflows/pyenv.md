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

Install dependencies

```
sudo apt-get update;
sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Install pyenv

```
curl https://pyenv.run | bash
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

Setup .bashrc

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

Make it available without restarting terminal

```
exec $SHELL
```

### Windows *TOTEST*

Install with PowerShell as administrator

```
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

Setup environment variable

```
PS C:\> $env:VAR_NAME="VALUE"
```

## Update

```
pyenv update
```

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


