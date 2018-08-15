#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CarefulWithThatPush
Yoji Watanabe
main.py

Driver for the CarefulWithThatPush command line tool.
"""

import argparse
import config
import ProjectTree


DIRTY_ARG = 'dirty'
CLEAN_ARG = 'clean'
CONFIG_ARG = 'config'


def parse_args():
    parser = argparse.ArgumentParser(description='A tool to help clean your code from possibly-sensitive information')
    parser.add_argument(dest='action', help='What action to be taken. \'init\' to configure this instance, \'clean\' to'
                                            ' remove sensitive information, and \'dirty\' to re-add sensitive '
                                            'information')

    return parser.parse_args()


def main():
    args = parse_args()

    git_info = ProjectTree.ProjectTree()

    if args.action.lower() == DIRTY_ARG:
        print "Dirtying it up"
    elif args.action.lower() == DIRTY_ARG:
        print "Cleaning up..."
    elif args.action.lower() == CONFIG_ARG:
        print "Setting up..."
        config.start_configuration(git_info.files)


# # # # # # # # # # # # # # #
if __name__ == "__main__":
    main()