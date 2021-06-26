import requests
print('1 - Проверить альбом по UPC\n2 - Проверить трек по upc')
s1 = int(input ('Выбери вариант: '))
if s1 == 1:
  s11 = input ('Введи UPC: ')
  URL = f'https://api.deezer.com/album/upc:{s11}'
  HEADERS = {
    'Accept': 'application/json, text/plain, */*'
  }
  r = requests.get(URL, HEADERS)
  data = r.json()
  DeezerId = data['id']
  upc = data['upc']
  title = data['title']
  Link = data['link']
  print(f'DEEZERID: {DeezerId}\n UPC: {upc} \nLink: {Link}')

if s1 == 2:
  s11 = input ('Введи UPC: ')
  URL = f'https://api.deezer.com/track/upc:{s11}'
  HEADERS = {
    'Accept': 'application/json, text/plain, */*'
  }
  req = requests.get(URL, HEADERS).json()
  print(req)
