__author__ = 'jcallen'


import json
import yaml
import sys
import os

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def main():
    arg = sys.argv[1:]
    json_file = open(arg[0], 'r')
    json_obj = json.load(json_file, encoding="latin-1")
    json_obj = byteify(json_obj)
    path = os.getcwd()

    for base_object in json_obj:
        if '.' not in base_object:
            new_directory = "%s/inventory/%s" % (path, base_object)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)

    for group_vars in json_obj['group_vars']:
        stream = open("%s/inventory/group_vars/%s" % (path, group_vars), "w")
        yaml.dump(json_obj['group_vars'][group_vars], stream, default_flow_style=False)
        stream.close()

    for host_vars in json_obj['host_vars']:
        stream = open("%s/inventory/host_vars/%s" % (path, host_vars), "w")
        yaml.dump(json_obj['host_vars'][host_vars], stream, default_flow_style=False)
        stream.close()

    stream = open("%s/inventory/hosts.ini" % path, "w")
    stream.write( json_obj['hosts.ini'] )
    stream.close()

if __name__ == '__main__':
    main()
