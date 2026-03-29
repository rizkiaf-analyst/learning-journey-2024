import requests
import pandas as pd 
import plotly.express as px

# Get historical BTC data from CoinDesk API
url = "https://api.coindesk.com/v1/bpi/historical/close.json"
response = requests.get(url)
data = response.json()

# Extract historical BTC data
historical_data = []
for date in data['bpi']:
    historical_data.append({
        'date': date,
        'close': data['bpi'][date]
    })

#def data():
    #url = "https://api.coindesk.com/v1/bpi/historical/close.json"
   # response = requests.get(url)
   #print(response.json())  
#data()


df = pd.DataFrame(historical_data)
print(df)
fig = px.line(df, title='BTC Price History', x='date', y='close')
fig.show()