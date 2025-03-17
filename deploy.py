import os
import sys

VERSION = '1.0.0'

if sys.platform == "win32":
    args = [
        'nuitka',
        '--standalone',
        '--windows-disable-console',
        '--plugin-enable=pyside6',
        '--include-qt-plugins=sensible,sqldrivers',
        '--assume-yes-for-downloads',
        # '--msvc=latest',              # Use MSVC
        '--mingw64',  # Use MinGW
        # '--show-memory',
        '--show-progress',
        '--windows-icon-from-ico=resources/images/PyDracula.ico',
        f'--windows-file-version={VERSION}',
        f'--windows-product-version={VERSION}',
        '--windows-file-description="Fluent UI"',
        '--output-dir=dist',
        '--remove-output',
        'app.py',
    ]
elif sys.platform == "darwin":
    args = [
        'python3 -m nuitka',
        '--standalone',
        '--plugin-enable=pyside6',
        '--include-qt-plugins=sensible,sqldrivers',
        '--show-memory',
        '--show-progress',
        "--macos-create-app-bundle",
        "--assume-yes-for-download",
        "--macos-disable-console",
        f"--macos-app-version={VERSION}",
        "--macos-app-name=Fluent-UI",
        "--macos-app-icon=resources/images/PyDracula.ico",
        '--output-dir=dist',
        'app.py',
    ]
else:
    args = [
        'pyinstaller',
        '-w',
        'app.py',
    ]

os.system(' '.join(args))
