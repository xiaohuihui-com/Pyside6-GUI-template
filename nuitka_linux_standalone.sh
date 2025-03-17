#!/usr/bin/env bash

#export QT_QPA_PLATFORM_PLUGIN_PATH=/home/alientek/anaconda3/envs/pyside6/lib/python3.11/site-packages/PySide6/Qt/plugins/platforms
python3 -m nuitka \
        --standalone \
        --mingw64 \
        --assume-yes-for-downloads \
        --enable-plugin=pyside6 \
        --include-qt-plugins=sensible,sqldrivers \
        --nofollow-imports \
        --output-dir=output \
        --show-progress \
        --remove-output \
        app.py