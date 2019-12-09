#!/usr/bin/python

import urllib3
from ansible.module_utils.basic import AnsibleModule


def get_status_code(url):
    con = urllib3.PoolManager()
    code = con.request('GET', url)
    return code.status

def main():
    fields = {"url": {"required": True, "type": "str"}}
    module = AnsibleModule(argument_spec=fields)
    code = get_status_code(module.params['url'])
    module.exit_json(msg=code)

if __name__ == '__main__':
    main()
