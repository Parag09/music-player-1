from cx_Freeze import setup, Executable

setup(name = 'music-player',
      version = '1.0',
      description = 'Created using Python 3.6',
      executables = [Executable("main.py")])
