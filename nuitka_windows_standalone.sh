#!/usr/bin/env bash

python -m nuitka \
        --standalone \
        --windows-console-mode=disable \
        --enable-plugin=pyside6 \
        --include-qt-plugins=sensible,sqldrivers \
        --windows-icon-from-ico=resources/images/PyDracula.ico \
        --nofollow-imports \
        --output-dir=output \
        --show-progress \
        --remove-output \
        app.py