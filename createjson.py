#!/usr/bin/python

import json
import yaml
import os
import fnmatch
import linecache
import sys
import pprint


def main():

    jsonobj = {}

    path = os.getcwd()
    yamlfiles = [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(path)
        for f in fnmatch.filter(files, '*.yml')]

    for yml in yamlfiles:
        with open(yml, 'r') as stream:
            temp = yml.replace(path,"")
            keys = temp.split('/')
            print keys
            ymlobj = yaml.load(stream)
            #jsonobj[keys[1]][[keys[2]] = ymlobj

            if keys[1] not in jsonobj:
                jsonobj[keys[1]] = {}
            jsonobj[keys[1]][keys[2]] = ymlobj


# finally our special case of hosts.ini

    with open('hosts.ini', 'r') as hosts:
        jsonobj['hosts.ini'] = hosts.read()

    with open('request.json', 'w') as request:
        json.dump(jsonobj, request)


if __name__ == '__main__':
    main()
