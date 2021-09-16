import json

with open('postinumerot.json') as f:
    sisalto = f.read()

numerot = json.loads(sisalto)

postinro = input('Kirjoita postinumero: ')

print(numerot[postinro])

 