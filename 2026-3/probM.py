import re
import requests
import tqdm
from bs4 import BeautifulSoup

session = requests.Session()
root_url = "http://173.249.53.220:54079/"
root = session.get(root_url)
hidden_vars = []
answers = [55, 29, 55, 48, 99, 48, 13112221, 87]
for i in tqdm.tqdm(range(10)):
  stage_url = root_url + f"fase/{i + 1}"
  stage = session.get(stage_url)
  if i < 8:
    payload = {"answer": str(answers[i])}
  elif i == 8:
    soup = BeautifulSoup(stage.text, features="html.parser")
    match = re.search(r"(\d+) significa \d+", soup.find("h3").text)
    payload = {"answer": match.group(1)}
  elif i == 9:
    soup = BeautifulSoup(stage.text, features="html.parser")
    expression = soup.find("h3").text.replace("×", "*").replace("−", "-")
    X = 0
    ans = exec(";".join(hidden_vars) + ";" + expression)
    payload = {"answer": X}
  answer = session.post(stage_url, data=payload)
  soup = BeautifulSoup(answer.text, features="html.parser")
  if i < 9:
    hidden_vars.append(soup.find("div", class_="hidden").text)
  else:
    for element in soup.find_all("h2"):
      if element.text.startswith("RQST"):
        final_answer = element.text

print(final_answer)
