import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

#Cases of error
try:
    html = urlopen(url)
except HTTPError as e:
    # HTTP Error
    print(e)
except URLError as e:
    # Incorrect URL
    print('The server could not be found!')

bs = BeautifulSoup(html, 'lxml')

# all 'trs' into '.lister-list' class
movies = bs.select('.lister-list tr')

titles = []
directors = []
years = []
ratings = []

for movie in movies:
    titles.append(movie.find('td', class_='titleColumn').find('a').get_text())
    directors.append(movie.find('td', class_='titleColumn').find('a')['title'])
    years.append(movie.find('td', class_='titleColumn').find('span').get_text()[1:5])
    ratings.append(movie.find('td', class_='imdbRating').find('strong').get_text())

df = pd.DataFrame({
    "title": titles,
    "year": years,
    "rating": ratings,
    "director": directors
})

# Ouputing top5 elements
#df.head()

# Saving in a csv file
df.to_csv('best_movies_imdb.csv')