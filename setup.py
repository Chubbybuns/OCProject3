from cx_Freeze import setup, Executable

buildOptions = dict(include_files=['Maze/', 'Consumables/', 'Characters/', 'Images/'])
setup(
     name="appname",
     version="1.0",
     description="MacGyver",
     author="Julia",
     options=dict(build_exe=buildOptions),
     executables=[Executable("Game.py")]
)
