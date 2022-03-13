from cx_Freeze import setup, Executable

base = None

executables = [Executable("Interface.py", base="Win32GUI")]

packages = ["idna", "tkinter", "ResultatDecimal"]
options = {
    'build_exe': {
        'packages': packages,
        "include_files": ["calculatrice.ico"]
    },
}

setup(
    name="Calculatrice by Pomme",
    options=options,
    version="1.1",
    description='Calculatrice, qui peut remplacer celle de google',
    executables=executables
)