#!/user/bin/env python3
# -*- coding: utf-8 -*-

from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['-F',
            '-w',
            '--paths=D:/py_workspace/test_demo',
            '--paths=D:/py_workspace/test_demo/ui',
            '--icon=D:/py_workspace/pims/stock_sync_tools/icon.ico',
            '--noupx',
            '--clean',
            'init.py']
    run(opts)