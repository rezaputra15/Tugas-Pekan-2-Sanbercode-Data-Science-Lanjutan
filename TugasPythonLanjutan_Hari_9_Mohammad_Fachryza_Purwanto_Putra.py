from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import pandas as pd

url = 'https://www1.gogoanime.movie/'
req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
data = bs(html, 'html.parser')

obyek = data.findAll('div', {'class' : 'last_episodes loaddub'})[0]
items = obyek.findAll('li')

judul = []
episode = []
index = 0
for item in items:
    nama = item.find('p', {'class' : 'name'})
    nama = nama.get_text().strip()
    judul.append(nama)
    ep = item.find('p', {'class' : 'episode'})
    ep = ep.get_text().strip()
    episode.append(ep)
    index +=1

df1 = pd.DataFrame(data=judul)
df2 = pd.DataFrame(data=episode)
df = pd.merge(df1, df2, left_index=True, right_index=True)
df.rename(columns = {'0_x' : 'Judul', '0_y': 'Episode Terakhir'}, inplace = True)
print(df)