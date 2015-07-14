#!/usr/bin/env python

import os
import fnmatch
import yaml
import linecache
import sys
from subprocess import Popen, PIPE
import argparse


def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="inventory")
    return parser.parse_args()


def main():

    args = command_line_arguments()

    variable = {}
    keys = []
    path = args.i

    yamlfiles = [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(path)
        for f in fnmatch.filter(files, '*.yml')]

    for yml in yamlfiles:
        with open(yml, 'r') as stream:
            vars = yaml.load(stream)
            keys += vars.keys()

    path = os.getcwd()
    yamlfiles = [os.path.join(dirpath, f)
                 for dirpath, dirnames, files in os.walk(path)
                 for f in fnmatch.filter(files, '*.yml')]


    for yml in yamlfiles:
        with open(yml, 'r') as stream:
            filestr = stream.read()
            for k in keys:
                if k not in variable:
                    temp = {k:False}
                    variable.update(temp)
                if k in filestr:
                    temp = {k:True}
                    variable.update(temp)


    print yaml.dump(variable, default_flow_style=False, allow_unicode=True)
if __name__ == '__main__':
    main()


