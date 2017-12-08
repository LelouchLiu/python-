import sys,os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = r'H:\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'H:\Python36-32\tcl\tk8.6'
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
#include_files = [r"H:\Python36-32\DLLs\tcl86t.dll",r"H:\Python36-32\DLLs\tk86t.dll"]
#packages=[r'G:\github\python-\tkinterS\manage',r"G:\github\python-\cfn\fileDeal"]

executables = [
    Executable('tkinterS/ui.py', base=base)
]

setup(name='simple_Tkinter',
      version='0.1',
      description='Sample cx_Freeze Tkinter script',
      options={"build_exe": {'path': sys.path + ['tkinterS']+['cfn']}},
      executables=executables
      )