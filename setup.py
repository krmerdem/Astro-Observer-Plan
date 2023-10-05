import sys
import os
from cx_Freeze import setup, Executable
import astropy

# Sanal ortamın içindeki 'lib' klasörünün yolu
virtual_env_lib = os.path.join(sys.prefix, 'Lib', 'site-packages')

files = ['icon/icon.ico']
astropy_path = os.path.join(astropy.__path__[0])
include_files = [(virtual_env_lib, 'lib'), (astropy_path, 'astropy')]

include_modules = [
    'astroquery',
    'astropy'
]

target = Executable(
    script="AstroObserverPlan.py",
    base="Win32GUI",
    icon="icon/icon.ico",
    shortcut_name='Astro OV',
    shortcut_dir="DesktopFolder"
)

setup(
    name="Astro Observer Plan",
    version="1.0",
    description="Astronomy Software",
    author="Kerem ERDEM, Korhan KARA",
    options={
        'build_exe': {
            'includes': include_modules,
            'include_files': include_files,
            'include_msvcr': True
        }
    },
    executables=[target],
)
