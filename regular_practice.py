# python regular expression practice
# parse the simple json string which has one nested structure.
# Demonstrate the following skills
# (1) lazy match -> .*?
# (2) re.DOTALL 

import re
data = """{
            "hello": "world",
            "key1": 20,
            "key2": 20.3,
            "foo": {
                "hello1": "world1",
                "key3": [200, 300]
            },
            "fuck": 1000
            }"""

reg = re.compile(r'("\w*"):(\s*{.*?}|[^,}]*)',re.DOTALL)
for match in  reg.findall(data):
    print match[0], match[1]
