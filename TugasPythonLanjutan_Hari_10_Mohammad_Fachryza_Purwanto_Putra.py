from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
data = bs(html, 'html.parser')

all_tables = data.findAll("table")
right_table = data.find("table", {"class" : "wikitable sortable"})

rank = []
visual = []
proper = []
p1 = []
p2 = []
distance = []
spectral = []

for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==7:
        rank.append(cells[0].get_text().strip())
        visual.append(cells[1].get_text().strip())
        proper.append(cells[2].get_text().strip())
        p1.append(cells[3].get_text().strip())
        p2.append(cells[4].get_text().strip())
        distance.append(cells[5].get_text().strip())
        spectral.append(cells[6].get_text().strip())

df = pd.DataFrame(rank,columns=['Rank'])
df['Visual Magnitude'] = visual
df['Proper Name'] = proper
df['Bayer Desig. part 1'] = p1
df['Bayer Desig. part 2'] = p2
df['Distance (ly)'] = distance
df['Spectral Class'] = spectral

#print(data.prettify())
# print(data.title)
# print(data.title.string)
print(df)
print(right_table)

df.to_excel(r"fachreyzaputra.xlsx", index=False)