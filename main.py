import requests
print('1 - Проверить альбом по UPC\n2 - Проверить трек по acrcloud')
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
  URL = f"https://eu-api-v2.acrcloud.com/api/music/search?per_page=20&page=1&q=upc:{l}"
  HEADERS = {
            'Access-Control-Allow-Origin': 'https://console.acrcloud.com',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3IiwianRpIjoiMTMyZWNjYzBmMzhkMTU2ODQ4ZGFmNGEyZTU3OTAzZWY3YTlhY2VjZjYxOTE4YmMyYzMxOGViYjkxMzJhZDBjNmE4ODgwNjViM2U2NTI1NDkiLCJpYXQiOjE2MjQ3MTA4ODguOTAxNjM4LCJuYmYiOjE2MjQ3MTA4ODguOTAxNjQxLCJleHAiOjE5NDAyNDM2ODguODYzNzcxLCJzdWIiOiIxMTc0MDEiLCJzY29wZXMiOlsiKiIsIndyaXRlLWFsbCIsInJlYWQtYWxsIiwiYnVja2V0cyIsIndyaXRlLWJ1Y2tldHMiLCJyZWFkLWJ1Y2tldHMiLCJhdWRpb3MiLCJ3cml0ZS1hdWRpb3MiLCJyZWFkLWF1ZGlvcyIsImNoYW5uZWxzIiwid3JpdGUtY2hhbm5lbHMiLCJyZWFkLWNoYW5uZWxzIiwiYmFzZS1wcm9qZWN0cyIsIndyaXRlLWJhc2UtcHJvamVjdHMiLCJyZWFkLWJhc2UtcHJvamVjdHMiLCJ1Y2YiLCJ3cml0ZS11Y2YiLCJyZWFkLXVjZiIsImRlbGV0ZS11Y2YiLCJibS1wcm9qZWN0cyIsImJtLWNzLXByb2plY3RzIiwid3JpdGUtYm0tY3MtcHJvamVjdHMiLCJyZWFkLWJtLWNzLXByb2plY3RzIiwiYm0tYmQtcHJvamVjdHMiLCJ3cml0ZS1ibS1iZC1wcm9qZWN0cyIsInJlYWQtYm0tYmQtcHJvamVjdHMiXX0.OsttA7DBIT9olqMDqaWK2NbAUI2aY01iWuFL8IWDfKNCeGH-cOXXx0ra_xY5V9TbslxsCVZX0RqSEbYg8C143T1xkadaGPpX3g86j1-I1l5tk18xhQKpM8J3WeV6W1BAsVw9ZiApoL0XHIJspKQFj35iICCI_9SVMP03ZGmRPjqmGXnwMrs7xbse5Xu5z6Rt92XuLY4ubbz-Y5wpRgNpZNOgd-zehgwRLXNQeStD_SdLlbiInE8Gnar6cFKumxuYlVCfXPxbN9DiWAYbj1-S3QhUmb77IIS_X_J7wB6CyHfmBlnEjtdb6UOio_KbkI4kc7Dz3zqO_nKZxBef1k6kGikFhWQNtbp0wXWCHD5Km4LPcYZLSc3pEtZ4GF7YYNLDpSoAV53xd6RxcS83UEaXifaT15nnsiZClBFhjyoCZqRL23ZLqSOaC_3NEW1L2O0IaWMdhQMMITDv9Qz6KhOYWvsfeLKoXFdInQ6TYPW5mxV2BmVVhLONBwdqf1oXpqkwr7Rwd1vqzgiXh7nXdKKRPcUUkqMy6SIfqEal3NkdOIjwveqBCNC1o3XG7hYfD1xD88qMD76DNpWRPAJXbsn_m7cZyngZ-q4NlcGS5iqCWkrsaKIbrRmU4pYElHqi0GgMGRrY1_H3ynA_dL3ZaWsVYeUf1UZQXLEzcsBDLKBCRVI'
            }

   r = requests.get(URL, headers=HEADERS)
   data = r.json()
   title = data['data'][0]['title']
   artist = data['data'][0]['duration_ms']
   s = data['data'][0]['artists'][0]['name']
   isrc = data['data'][0]['external_ids']['isrc'][0]          
   upc = data['data'][0]['external_ids']['upc'][0]
   ars = data['data'][0]['label']

   d = timedelta(milliseconds=artist)

   print(Title - {title} \n Artist - {s} \n Duration - {d} \n Upc : {upc} )
   print('Created by t.me/nikprotect')
 
