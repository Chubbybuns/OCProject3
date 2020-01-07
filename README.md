# OCProject3

## Install

1) `git clone https://github.com/Julialin17/OCProject3`
2) `python -m venv 'nom du venv'` (pour créer un environnement virtuel)
3) `"nom du venv" \Scripts\activate.bat` (pour activer l'environnement virtuel)
4) `python –m pip install –r requirements.txt` (pour installer les librairies requises)

## Launch

`python Game.py`

## Build

Create setup.py file:

```
from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ['Maze/', 'Consumables/', 'Characters/', 'Images/'])
setup(
         name = "appname",
         version = "1.0",
         description = "MacGyver",
         author = "Julia",
         options = dict(build_exe = buildOptions),
         executables = [Executable("Game.py")])
```

`python setup.py build`
