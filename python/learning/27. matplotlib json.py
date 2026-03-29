import requests
import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.DataFrame(historical_data)
df.plot(kind='line')
plt.plot(df['date'], df['close'])
plt.title('Historical Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()