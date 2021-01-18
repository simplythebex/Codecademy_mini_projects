#Hair salon data

#name of hairstyle
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"] 

#price of each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35] 

#number of each hairstyle cut
last_week = [2, 3, 5, 8, 4, 4, 6, 2] 

#total of all prices 
total_price = 0

for price in prices:
  total_price += price

#average price
average_price = total_price/len(prices)
print("Average Haircut Price: £" + str(average_price))

#make each haircut £5 cheaper
new_prices = [price - 5 for price in prices]
print("New, cheaper prices are: " + str(new_prices))

# total revenue from the week
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: £" + str(total_revenue))

# average revenue from each day over the week
average_daily_revenue = total_revenue / 7
print("Average daily revenue is: £" + str(average_daily_revenue))

# finding haircuts under £30 after price decrease
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print("Haircuts for under £30: " + str(cuts_under_30))