import pandas as pd
import matplotlib.pyplot as plt
Index = pd.read_csv("C:/Users/BRAILER/Downloads/S&P 500 Historical Data.csv")
print(Index.head())
Index["Date"] = pd.to_datetime(Index["Date"], format="%m/%d/%Y")
# Convert numerical columns to float (removing commas)
numerics = ["Price", "Open", "High", "Low"]
Index[numerics] = Index[numerics].replace(",", "", regex=True).astype(float)

# Convert 'Change %' to float after removing the percentage sign
Index["Change %"] = Index["Change %"].str.replace("%", "").astype(float)

# Sort data in ascending order (older dates first)
Index = Index.sort_values("Date")

# Plot the Closing Price over time
plt.figure(figsize=(12, 6))
plt.plot(Index["Date"], Index["Price"], label="S&P 500 Price", color="blue")

# Formatting
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("S&P 500 Historical Closing Prices")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
