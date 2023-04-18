# Programa de configuração para o cx_Freeze poder "Buildar"
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"],
                     "includes": ["tkinter","numpy","matplotlib","PIL"],
                     "include_files": ["imagens","img.ico"]}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="ORABOLAS",
    version="1.0",
    description="projeto",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="plot.py", base=base, icon="img.ico")]
)