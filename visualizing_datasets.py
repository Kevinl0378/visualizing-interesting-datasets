####### JSON #######
import json
import matplotlib.pyplot as plt

paths = ['Project_02/china_gdp.json']
raw_gdp_data = []
for path in paths:
    with open(path, encoding = 'ascii') as f:
        text = f.read()
        raw_gdp_data += json.loads(text)
gdp_data = raw_gdp_data[1]

years = []
for data in gdp_data:
    year = data['date']
    years.append(year)
years.sort() # Start: 1960, End: 2021
years_int = []
for year in years:
    year_int = int(year)
    years_int.append(year_int)


gdps = []
for data in gdp_data:
    gdp = data['value']
    gdps.append(gdp)
gdps = gdps[::-1]
# Another method
sorted_gdps = []
for year in years:
    for data in gdp_data:
        if data['date'] == year:
            sorted_gdps.append(data['value'])
# print(gdps==sorted_gdps) # Returns True 
gdp_scaled = []
for gdp in sorted_gdps:
    new_gdp = gdp / 1000000000
    gdp_scaled.append(new_gdp)

plt.plot(years_int, gdp_scaled, marker = 'o', markersize = 3, color = 'green')
plt.xticks(range(min(years_int), max(years_int), 10))
plt.yticks(range(0, 19000, 1500))
plt.xlabel("Year")
plt.ylabel("GDP (billions of U.S. dollars)")
plt.show()



####### CSV #######
import csv
import matplotlib.pyplot as plt

netflix_File = open('Project_02/netflix_titles.csv')
netflix_Reader = csv.reader(netflix_File)
raw_netflix_titles = list(netflix_Reader)
#print(raw_netflix_titles[0].index('release_year'))   # Returns index 7
#print(raw_netflix_titles[0].index('type'))   # Returns index 1
netflix_titles = raw_netflix_titles[1:]

netflix_movies_release = []
netflix_tv_release = []
for title in netflix_titles:
    if title[1] == "Movie":
        netflix_movies_release.append(title[7])
    if title[1] == "TV Show":
        netflix_tv_release.append(title[7])

movie_int = []
for movie in netflix_movies_release:
    release = int(movie)
    movie_int.append(release)

tv_int = []
for tv in netflix_tv_release:
    release = int(tv)
    tv_int.append(release)

plt.hist(movie_int, bins = max(movie_int) - min(movie_int) + 1, alpha = 0.5, label = 'Movies', edgecolor = 'black', color = 'navy')
plt.hist(tv_int, bins = max(tv_int) - min(tv_int) + 1, alpha = 0.5, label = "TV Shows", edgecolor = 'black', color = 'red')
plt.legend(loc = 'upper left')
plt.xticks(range(1920, 2025, 10))
plt.yticks(range(0, 850, 50))
plt.xlabel("Release Year")
plt.ylabel("Number of Titles", labelpad = 7)
plt.show()













