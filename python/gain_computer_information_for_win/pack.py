#!/user/bin/env python3
# -*- coding: utf-8 -*-

from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['-F',
            '-w',
            '--paths=D:/demo',
            '--paths=D:/demo/ui',
            '--noupx',
            '--clean',
            'init.py']
    run(opts)
