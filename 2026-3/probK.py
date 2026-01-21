import base64
import re
import requests

root_url = "http://173.249.53.220:39985/"
text = requests.get(root_url).text
encoded = re.search(r"Complete flag: (.+?=)", text).group(1)
print(base64.b64decode(encoded).decode("utf-8"))

