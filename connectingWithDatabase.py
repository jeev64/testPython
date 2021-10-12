import pandas as pd

html_url = 'https://www.basketball-reference.com/leagues/NBA_2019.html'
nba_tables = pd.read_html(html_url)
print(len(nba_tables))
nba = nba_tables[0]
print(nba)
#nba.head()
#print(nba.head())

