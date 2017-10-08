import pandas as pd

def parse_data(data):
    cols_to_keep = ['hometeam', 'awayteam', 'fthg', 'ftag', 'b365h', 'b365d', 'b365a']
    data.columns = data.columns.str.lower()
    data = data[cols_to_keep]
    
    teams = (data['hometeam']
         .drop_duplicates()
         .reset_index(drop=False)
         .assign(i = lambda x: x.index)
         .drop('index', axis=1)
         .rename(columns={'hometeam': 'team'})
         )
    
    df = (pd.merge(data, teams, left_on='hometeam', right_on='team')
      .rename(columns={'i': 'i_home'})
      .drop('team', axis=1)
      )

    df = (pd.merge(df, teams, left_on='awayteam', right_on='team')
      .rename(columns={'i': 'i_away'})
      .drop('team', axis=1)
      )
    
    df = df.dropna()
    
    return df, teams

