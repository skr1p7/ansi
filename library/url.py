#!/usr/bin/python3

import urllib3
from ansible.module_utils.basic import *

def main():
    http = urllib3.PoolManager()
	module = AnsibleModule(argument_spec={"url": {"required": True, "type": "str" }})
    response = http.request(module.params["url"])
    module.exit_json(changed=True, meta={"return_code":response.code})

if __name__ == '__main__':
    main()


