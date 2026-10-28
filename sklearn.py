import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Provide Training Data (Features = Size in sq ft, Labels = Price in $1000s)
# 1000 sq ft -> $200k, 1500 sq ft -> $300k, etc.
house_sizes = np.array([[1000], [1500], [2000], [2500], [3000]])
house_prices = np.array([200, 300, 400, 500, 600])

# 2. Initialize the AI Model (Linear Regression)
ai_model = LinearRegression()

# 3. Train the AI (This is where it learns the pattern/rule)
ai_model.fit(house_sizes, house_prices)

# 4. Use the AI to predict the price of a completely new house
new_house_size = np.array([[1800]]) # A house size the AI hasn't seen yet
predicted_price = ai_model.predict(new_house_size)

# 5. Output the result
print(f"🏠 For a house of {new_house_size[0][0]} sq ft...")
print(f"💰 The AI predicts the price will be: ${predicted_price[0]:.2f}K (or ${predicted_price[0]*1000:,.2f})")