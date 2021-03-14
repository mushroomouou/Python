import requests
from pprint import pprint

name = {
    "name": "hezhi",
    "age": 20
}
response = requests.get("http://httpbin.org/get",params=name)

pprint("状态码： {}".format(response.status_code))
pprint(response.text)

