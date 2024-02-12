# Python
import pandas as pd
from prophet import Prophet


df = pd.read_csv("data_converted/Retail_converted.csv",header=0)
# Python
print(df.info())
df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].astype(float)
df.columns = ['ds', 'y']
m = Prophet()
df2 = df.iloc[:1000,2:]
model = Prophet()
model.fit(df2)

# Make predictions
future_dates = model.make_future_dataframe({'ds': pd.date_range(start=df['ds'].iloc[-1], periods=30)})  # Generate 30 days of future dates
predictions = model.predict(future_dates)

# Plot the results
model.plot(predictions)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Predicted Values')
plt.show()