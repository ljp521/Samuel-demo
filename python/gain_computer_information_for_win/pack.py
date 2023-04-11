#!/user/bin/env python3
# -*- coding: utf-8 -*-

from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['-F',
            '-w',
            '--paths=D:/demo', # 请自行修改路径
            '--paths=D:/demo/ui',# 请自行修改路径
            '--noupx',
            '--clean',
            'init.py']
    run(opts)
