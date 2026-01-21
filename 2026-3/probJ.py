import codecs
import hashlib
import more_itertools as mi
import base64
import re
import requests
from bs4 import BeautifulSoup

root_url = "http://173.249.53.220:42807/"
session = requests.Session()
login_data = {"username": "admin", "password": "admin_password"}
text = session.post(root_url + "login", data=login_data).text

fragments = []
bundle = session.get(root_url + "static/dashboard.js").text
encoded = re.search(r'\("(.+?)"\)', bundle).group(1)
fragments.append(base64.b32decode(encoded[::-1]).decode('utf-8'))

audit = session.get(root_url + "api/audit").json()
trace_hex = audit["events"][0]["trace_hex"]
split_hex = [chr(int("".join(x), 16)) for x in mi.chunked(trace_hex, 2)]
fragments.append("".join(split_hex))

prefs = session.post(root_url + "api/prefs")
for cookie, val in session.cookies.items():
  if cookie.startswith("pref_r13"):
    fragments.append(codecs.encode(val, "rot_13"))

security = session.get(root_url + "dashboard/security")
slot = base64.b64decode(security.headers["x-slot-b64"]).decode("utf-8")
soup = BeautifulSoup(security.text, features="html.parser")
for code in soup.find_all("code"):
  if code.text.startswith("md5"):
    md5_encoded = code.text.split(" = ")[1]
    for pin in range(10000):
      md5 = hashlib.new("md5")
      full_pin = ("0000" + str(pin))[-4:]
      md5.update(full_pin.encode("utf-8"))
      if md5.hexdigest() == md5_encoded:
        fragments.append(f"{slot}:{full_pin}")

overview = session.get(root_url + "dashboard/overview")
decoded = base64.b64decode(overview.headers["x-frag-b64"]).decode("utf-8")
fragments.append(decoded)

keyring_data = {"fragments": "\n".join(fragments)}
keyring = session.post(root_url + "dashboard/keyring", data=keyring_data)

fragments.sort()
master_code = "".join(f.split(":")[1] for f in fragments).replace("0", "")
vault = session.post(root_url + "vault", data={"code": master_code})
soup = BeautifulSoup(vault.text, features="html.parser")
for h1 in soup.find_all("h1"):
  if h1.text.startswith("RQST"):
    print(h1.text)
