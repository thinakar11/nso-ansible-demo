#!/usr/bin/env python

import json
import sys
import yaml

def _utf8_encode(obj):
    if obj is None:
        return None
    if sys.version_info[0] > 2:  # PY3
        if isinstance(obj, str):  # in py3 str is unicode
            return obj
    else:                       # PY2
        if type(obj) is unicode:  # in py2 unicode
            return obj.encode('utf-8')

    if type(obj) is list:
        return [_utf8_encode(value) for value in obj]
    if type(obj) is dict:
        obj_dest = {}
        if sys.version_info[0] > 2:  # PY3
            for key, value in obj.items():
                obj_dest[_utf8_encode(key)] = _utf8_encode(value)
        else:
            for key, value in obj.iteritems():  # py2 obj.iteritems
                obj_dest[_utf8_encode(key)] = _utf8_encode(value)
        return obj_dest
    return obj



def main():
    obj = json.load(sys.stdin)
    utf8_obj = _utf8_encode(obj)
    yaml.dump({'top': utf8_obj}, stream=sys.stdout,
              default_flow_style=False, explicit_start=False)


if __name__ == '__main__':
    main()
