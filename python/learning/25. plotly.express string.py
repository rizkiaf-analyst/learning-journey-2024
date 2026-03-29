import pandas as pd 
import plotly.express as px

data = {
        "2024-03-26": 70074.4977,
        "2024-03-27": 69482.711,
        } 


for date in data:
    print(date)



historical_data = []
for date in data:
    historical_data.append({
        'date': date,
        'close': data[date]
    })

print(historical_data)

df = pd.DataFrame(historical_data)

fig = px.line(df, title='BTC Price History', x='date', y='close')
#fig.show()