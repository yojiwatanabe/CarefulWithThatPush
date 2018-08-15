#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CarefulWithThatPush
Yoji Watanabe
main.py

Driver for the CarefulWithThatPush command line tool.
"""

import subprocess


class ProjectTree(object):
    def __init__(self):
        self._files = self.get_git_files()

    @property
    def files(self):
        return self._files

    # get_git_files()
    #
    # Gets the file names for all tracked files in the current git repository.
    @staticmethod
    def get_git_files():
        out = ''
        try:
            # Open subprocess to list git files, get its output
            process = subprocess.Popen(['git', 'ls-tree', '--full-tree', '-r', 'HEAD', '--name-only'],
                                       stdout=subprocess.PIPE)
            out, err = process.communicate()
        except Exception as e:
            print '### ERROR\n' + str(e)

        return out.split()
